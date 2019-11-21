from django.shortcuts import render

from home.models import CrawlData,CrawModel,EmotionKeyword
from form_util import get_paramer
import json
from other.pager import Pager


# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def hello(request,):

    context = get_paramer(request)
    
    datas=CrawlData.objects.all()

    datas = datas.exclude(status=0)
    if context.get('start_date','') !='':
        datas = datas.filter(publish_time__gte=context['start_date'])
    if context.get('end_date','') !='':
        datas = datas.filter(publish_time__lte=context['end_date'])
    if context.get('source','') !='':
        datas = datas.filter(source=context['source'])
    if context.get('emotion','') !='':
        datas = datas.filter(emotion=context['emotion'])

    totalCounts = datas.count()
    currentPage = int(context.get('currentPage', 1))
    context = Pager.get_pagecontext(context,totalCounts,currentPage)


    context['datas'] = []
    if currentPage !=0:
        context['datas'] = datas.order_by('-publish_time')[(currentPage-1)*Pager.pagesize:currentPage*Pager.pagesize]

    print(context)
    return render(request,'home/query.html',context)


# 热点新闻分析
def wordcloud(request):
    context = get_paramer(request)


    datas = CrawlData.objects.all()
    if context.get('start_date', '') != '':
        datas = datas.filter(publish_time__gte=context['start_date'])
    if context.get('end_date', '') != '':
        datas = datas.filter(publish_time__lte=context['end_date'])
    if context.get('emotion','') !='':
        datas = datas.filter(emotion=context['emotion'])
    print(context,datas.count())



    dic_ = {}
    for d in datas.all():
        ks = d.keywords.split('；')
        for k in ks:
            if k not in dic_:
                dic_[k]=0
            dic_[k]+=1

    limit = int(context.get('limit',100))
    min_limit = int(context.get('min_limit',1))
    context['limit']=limit
    context['min_limit']=min_limit

    s = sorted(dic_.items(),key=lambda x:x[1],reverse=True)[:limit]
    keys = {}
    for k in s:
        is_num = False
        try:
            int(k[0])
            is_num=True
        except:
            pass
        if k[0]=='' or is_num or k[1]<=min_limit:
            continue
        keys[k[0]]=k[1]

    context['json_data']=json.dumps(keys,ensure_ascii=False)

    return render(request,'wordcloud.html',context)





import news_analysis
import json
def showdetail(request):
    id = request.GET['id']
    d = CrawlData.objects.get(id=id)
    if d.keywords =='' or d.product_name is None:
        news_analysis.news_analysis(id)
        d = CrawlData.objects.get(id=id)
    context = {}
    context['data'] = d

    context['names'] = json.loads(d.product_name)
    context['names'].pop('all')
    context['industry']=json.loads(d.industry)
    context['industry'].pop('all')
    return render(request,'home/showdetail.html',context)


from django.db.models import  Count
from django.db.models.functions import Substr
def trend_index(request, ):

    context = get_paramer(request)

    datas = CrawlData.objects.all()

    if context.get('start_date', '') != '':
        datas = datas.filter(publish_time__gte=context['start_date'])
    if context.get('end_date', '') != '':
        datas = datas.filter(publish_time__lte=context['end_date'])
    if context.get('emotion','') !='':
        datas = datas.filter(emotion=context['emotion'])

    print(datas.count())

    i = 10
    if context.get('countType')=='month':
        i = 7

    ll = datas.values('publish_time').annotate(date=Substr('publish_time',1,i)).values('date').annotate(count=Count('date')).order_by('date')
    line ={}
    for i in ll:
        if i['date'] is None:
            continue
        line[i['date']]=i['count']
        if line[i['date']]<100:
            line[i['date']] *=3



    context['line']=json.dumps(line,ensure_ascii=False)


    return render(request, 'trend/query.html', context)



def source_index(request, ):

    context = get_paramer(request)

    datas = CrawlData.objects.all()

    if context.get('start_date', '') != '':
        datas = datas.filter(publish_time__gte=context['start_date'])
    if context.get('end_date', '') != '':
        datas = datas.filter(publish_time__lte=context['end_date'])
    if context.get('emotion','') !='':
        datas = datas.filter(emotion=context['emotion'])


    ll = datas.values('source').annotate(count=Count('source'))
    dic_={}
    for i in ll:
        if i['source'] is None:
            continue
        dic_[i['source']] = i['count']
    context['source']=json.dumps(dic_,ensure_ascii=False)


    return render(request, 'source/query.html', context)



def source_list(request, ):

    context = get_paramer(request)

    datas = CrawModel.objects.all()

    if context.get('source', '') != '':
        datas = datas.filter(web_name__gte=context['source'])


    totalCounts = datas.count()
    currentPage = int(context.get('currentPage', 1))
    context = Pager.get_pagecontext(context,totalCounts,currentPage)


    context['datas'] = []
    if currentPage !=0:
        context['datas'] = datas[(currentPage-1)*Pager.pagesize:currentPage*Pager.pagesize]
    print(context['datas'])



    return render(request, 'source/list.html', context)





from other.area import  province_lat_lng,county_lat_lng,city_lat_lng
#
def emotion_index(request, ):

    context = get_paramer(request)

    datas = CrawlData.objects.all().filter(emotion=1)

    if context.get('start_date', '') != '':
        datas = datas.filter(publish_time__gte=context['start_date'])
    if context.get('end_date', '') != '':
        datas = datas.filter(publish_time__lte=context['end_date'])



    names_dict,industry_dict,area_dict={},{},{}

    def count(jsons,dict_):

        try:
            d = json.loads(jsons)
        except:
            pass
            return

        for i in d.keys():
            if i=='all':
                continue
            if i not in dict_:
                dict_[i]=0
            dict_[i]+=1

    def filter_dict(dic,limit):

        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        dic = dic[:limit]
        r = {}
        for i in dic:
            r[i[0]]=i[1]
        return r

    for i in datas:
        n = i.product_name
        count(n,names_dict)
        n = i.industry
        count(n, industry_dict)

        n = i.area
        if n=='' or n is None:
            continue
        n = json.loads(n)
        count(json.dumps(n[context.get('area','province')],ensure_ascii=False), area_dict)

    print(area_dict)

    limit = int(context.get('limit',10))
    names_dict = filter_dict(names_dict,limit)
    industry_dict = filter_dict(industry_dict,limit)

    context['names']=json.dumps(names_dict,ensure_ascii=False)
    context['industrys'] = json.dumps(industry_dict, ensure_ascii=False)

    context['areas'] = json.dumps(area_dict, ensure_ascii=False)

    area_level = context.get('area','province')
    lat_lng = {}
    if area_level =='province':
        lat_lng = province_lat_lng
    elif area_level =='county':
        lat_lng = county_lat_lng
    else:
        lat_lng = city_lat_lng


    area_data = []
    geo_data = {}

    for area in area_dict:
        t = {'name':area,'value':area_dict[area]}
        geo = lat_lng.get(area,'')
        if geo =='':
            continue
        area_data.append(t)
        geo_data[area]=geo

    context['area_data'] = json.dumps(area_data, ensure_ascii=False)
    context['geo_data'] = json.dumps(geo_data, ensure_ascii=False)

    print(context)
    return render(request, 'emotion/query.html', context)







    return render(request, 'source/list.html', context)






def emotionkey_index(request,):


    context = get_paramer(request)

    datas = EmotionKeyword.objects.all()

    context['datas']=datas

    return render(request, 'set/query.html', context)



