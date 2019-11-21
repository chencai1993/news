

from home_crawldata import HomeCrawldata
import datetime
ll = HomeCrawldata.filter(industry__eq=None)
ll = HomeCrawldata.filter(id__gt=0)
def get_time(s):

    fs = ['%Y-%m-%d','%Y-%m-%d %H:%M:%S','%Y年%m月%d','%Y年%m月%d日','%Y年%m月%d日 %H:%M']
    for f in fs:
        try:
            d = datetime.datetime.strptime(s,f)
            return d.strftime('%Y-%m-%d %H:%M:%S')
        except:
            pass
    print(s)
    return None




for p in ll:

    p.publish_time = get_time(p.publish_time)
    p.save()


#get_time('2019-03-17 13:52:00')