
from home_crawldata import HomeArea,HomeCrawldata
import pandas as pd



from jieba import analyse

tfidf = analyse.extract_tags

province,city,county = set(),set(),set()
name_code={}
code_name={}


province_lat_lng ={}
city_lat_lng ={}
county_lat_lng ={}

'''
l = HomeArea.filter(HomeArea.code ** '%0000')
def filter(s):
    s = s.replace('回族自治区','')
    s = s.replace('维吾尔自治区', '')
    s = s.replace('壮族自治区', '')
    s = s.replace('自治区', '')
    s = s.replace('省', '')
    s = s.replace('市', '')
    return s
for i in l:
    p = filter(i.province)
    name_code[p]= i.code[:2]
    code_name[i.code[:2] ] = p
    province.add(p)

    province_lat_lng[p]=[i.lat,i.lng]




l = HomeArea.filter(HomeArea.code ** '%00')

'''
def filter(s):
    for i in ['市']:
        if s[-len(i):]==i:
            s = s.replace(i, '')
    return s

'''
for i in l:
    if i.county not in ['市辖区','区','城区','县'] and i.code[-4:]!='0000':
        c = filter(i.county)
        name_code[c]= i.code[:4]
        code_name[i.code[:4]]=c
        county.add(c)
        county_lat_lng[c]=[i.lat,i.lng]
'''

# l = HomeArea.select()
def filter(s):

    return s

'''
for i in l:
    if i.city not in ['市辖区','区','城区','县','省直辖行政单位','市中区','城区','郊区','矿区','城中区']  and i.code[-2:]!='00':
        c = filter(i.city)
        name_code[c]= i.code
        code_name[i.code] = c
        city.add(c)

        city_lat_lng[c] = [i.lat,i.lng]
'''








import  json

def get_areas(content):

    city_list,county_list,province_list = {},{},{}
    for c in city:
        count = content.count(c)
        if count>0:
            city_list[c]=count
            try:
                county_list[code_name[name_code[c][:4]]]=count
            except:
                province_list[code_name[name_code[c][:2]]] = count

    for c in county:
        count = content.count(c)
        if count>0:
            if c not in county_list:
                county_list[c]=0
            county_list[c]+=count
            try:
                province_list[code_name[name_code[c][:2]]]=count
            except:
                print(c)

    for c in province:
        count = content.count(c)
        if count>0:
            if c not in province_list:
                province_list[c]=0
            province_list[c]+=count
    r = {
        'province':province_list,
        'county':county_list,
        'city':city_list
    }
    r = json.dumps(r,ensure_ascii=False)
    return r






def cucalute_one(id):
    #try:
        print('get areas start')
        d = HomeCrawldata.get_by_id(id)
        d.area = get_areas(d.content)
        d.save()
        print('get areas end')
    #except:
    #    print('关键词提取计算出错')


def update_all():
    ll = HomeCrawldata.filter(area__eq=None)
    for p in ll:
        c = get_areas(p.content)
        p.area = c
        print(c)
        p.save()


if __name__ =='__main__':
    i=1
    #update_all()


