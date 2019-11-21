from django.shortcuts import render
from form_util import to_json
import json
from home.models import CrawlData

def showwordcloud(request):
    context = {}
    p = {}
    try:
        p = to_json(request)
        print(p)
    except:
        pass

    datas = CrawlData.objects.all()
    if p.get('start_date', '') != '':
        datas = datas.filter(publish_time__gte=p['start_date'])
    if p.get('end_date', '') != '':
        datas = datas.filter(publish_time__lte=p['end_date'])



    dic_ = {}
    for d in datas:
        ks = d.keywords.split('；')
        for k in ks:
            if k not in dic_:
                dic_[k]=0
            dic_[k]+=1
    return json.dumps(dic_)


