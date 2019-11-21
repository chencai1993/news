
from home_crawldata import HomeCrawldata
import pandas as pd



from jieba import analyse

tfidf = analyse.extract_tags


def get_keywords(content,n):
    keywords = tfidf(content,allowPOS =('n','nr','ns','nt','nz','v','vn'))[:n]
    return '；'.join(keywords)

def cucalute_one(id):
    try:
        print('get keywords start')
        d = HomeCrawldata.get_by_id(id)
        d.keywords = get_keywords(d.content,6)
        d.save()
        print('get keywords end')
    except:
        print('关键词提取计算出错')



def update_all():
    ll = HomeCrawldata.filter(keywords__eq='')
    for p in ll:

        c = get_keywords(p.content,6)
        p.keywords = c

        p.save()

    ll = HomeCrawldata.filter(keywords__eq=None)
    for p in ll:
        c = get_keywords(p.content, 6)
        p.keywords = c

        p.save()




if __name__ =='__main__':
    update_all()


