from home_crawldata import HomeCrawldata

def update_all():
    ll = HomeCrawldata.filter(id__gt=0)
    for p in ll:
        if p.industry =='{"all": 0}':
            p.status=0
            p.save()
if __name__ == '__main__':
    update_all()