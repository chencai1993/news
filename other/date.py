
from other.home_crawldata import HomeCrawldata
import pandas as pd






def get_date(content):

    if content is None:
        return content
    content = content.replace('年','-')
    content = content.replace('月', '-')
    content = content.replace('日', '')

    if len(content.split('-')[0])==2:
        content='20'+content
    content=content[:len('2019-01-01 10:11')]
    return content



def cucalute_one(id):
    #try:
        print('get cate start')
        d = HomeCrawldata.get_by_id(id)
        d.publish_time = get_date(d.publish_time)
        d.save()
        print('get cate start')
    #except:
        print('名称识别出错计算出错')



def update_all():

    ll = HomeCrawldata.filter(id__gt=0)

    for p in ll:
        p.publish_time = get_date(p.publish_time)
        p.save()

if __name__ =='__main__':
    update_all()














