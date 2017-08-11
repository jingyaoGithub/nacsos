import django, re, gc

from multiprocess import Pool
from functools import partial



from scoping.models import *
from tmv_app.models import *

##################################
## Flatten nested lists

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


###################################
# function, to be done in parallel,
# which pull citations from docs,
# adds them to db,
# and links citations and docs

def doc_cites(doc):
    django.db.connections.close_all()
    citations = doc.wosarticle.cr
    cdos = []
    for c in citations:

        doim = re.findall("DOI ([0-9]+.*)",c)
        if len(doim) > 0:
            doi = doim[0].replace(" ","")
            cobject, created = Citation.objects.get_or_create(
                doi = doi
            )
            if created:
                cobject.ftext = c
                cobject.save()
            #otherise append to alt text
        else:
            cobject, created = Citation.objects.get_or_create(
                ftext = c
            )

        cdo = CDO(doc=doc,citation=cobject)
        cdos.append(cdo)
    return(cdos)


def shingle(text):
    return set(s for s in ngrams(text.lower().split(),2))

def get(r, k):
    try:
        x = r[k]
    except:
        x = ""
    return(x)

def jaccard(s1,s2):
    try:
        return len(s1.intersection(s2)) / len(s1.union(s2))
    except:
        return 0


def add_doc(r, q, update):

    django.db.connections.close_all()

    doc, created = Doc.objects.get_or_create(UT=r['UT'])

    if created==False and update==False:
        doc.query.add(q)
    else:
        doc.title=get(r,'TI')
        doc.content=get(r,'AB')
        doc.PY=get(r,'PY')
        doc.wos=True
        doc.save()
        doc.query.add(q)
        article, created = WoSArticle.objects.get_or_create(doc=doc)
        try:
            r['wc'] = [x.strip() for x in get(r,'WC').split(";")]
        except:
            pass
        r['kwp'] = get(r,'ID')
        r['iss'] = get(r,'IS')
        for field in r:
            f = field.lower()
            try:
                article.f = r[field]
                setattr(article,f,r[field])
                #article.save()
                #print(r[field])
            except:
                print(field)
                print(r[field])

        article.save()


        ## Add authors
        # try:
        if get(r,'AU') == "":
            return

        for a in range(len(r['AU'])):
            try:
                af = r['AF'][a]
            except:
                af = None
            au = r['AU'][a]
            if 'C1' not in r:
                r['C1'] = [""]
            a_added = False
            for inst in r['C1']:
                inst = inst.split('] ',1)
                iauth = inst[0]
                # try:
                if len(inst) == 1:
                    if len(r['AU'])==1:
                        institute = inst
                        iauth = af
                else:
                    institute = inst[1]
                if af in iauth:
                    try:
                        dai,created = DocAuthInst.objects.get_or_create(
                            doc=doc,
                            AU = au,
                            AF = af,
                            institution = institute,
                            position = a+1
                        )
                        dai.save()
                        a_added=True
                    except:
                        doc.docauthinst_set.all().delete()
                        dai,created = DocAuthInst.objects.get_or_create(
                            doc=doc,
                            AU = au,
                            AF = af,
                            institution = institute,
                            position = a+1
                        )
                        dai.save()
                        a_added=True
                        print("{} {} {} {} {}".format(doc,au,af,institute,a+1))
            if a_added == False: # i.e. if there is nothing in institution...
                dai, created = DocAuthInst.objects.get_or_create(
                    doc=doc,
                    AU = au,
                    AF = af,
                    position = a+1
                )
                dai.save()
        # except:
        #     pass


def read_wos(res, q, update):
    i=0
    n_records = 0
    records=[]
    record = {}
    mfields = ['AU','AF','CR','C1','WC']

    max_chunk_size = 2000
    chunk_size = 0

    p=12

    for line in res:
        if '\ufeff' in line: # BOM on first line
            continue
        if line=='ER\n':
            # end of record - save it and start a new one
            n_records +=1
            records.append(record)
            record = {}
            chunk_size+=1
            if chunk_size==max_chunk_size:
                # parallely add docs
                pool = Pool(processes=p)
                pool.map(partial(add_doc, q=q, update=update),records)
                pool.terminate()
                records = []
                chunk_size = 0
            continue
        if re.match("^EF",line): #end of file
            if chunk_size < max_chunk_size:
                # parallely add docs
                pool = Pool(processes=p)
                #pool.map(update_doc, records)
                pool.map(partial(add_doc, q=q, update=update),records)
                pool.terminate()
            #done!
            break
        if re.match("(^[A-Z][A-Z1-9])",line):
            s = re.search("(^[A-Z][A-Z1-9]) (.*)",line)
            key = s.group(1).strip()
            value = s.group(2).strip()
            if key in mfields:
                record[key] = [value]
            else:
                record[key] = value
        elif len(line) > 1:
            if key in mfields:
                record[key].append(line.strip())
            else:
                record[key] += " " + line.strip()

    return n_records