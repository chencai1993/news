
from other.home_crawldata import HomeCrawldata
import pandas as pd
def load():
    df = pd.read_csv('cate_name.csv',sep=',',encoding='gbk')
    s = set()
    for i in range(df.shape[0]):
        t = df.name.iloc[i].split(';')
        for j in t:
            s.add(j)
    s = list(s)
    import jieba
    jieba.load_userdict(s)



    name_to_cate = {}
    for i in range(df.shape[0]):
        name = df['name'][i]
        cate = df['cate'][i]
        names = name.split(';')
        for n in names:
            if n =='牛':
                print(i)
            name_to_cate[n]=cate
    return name_to_cate

import json
def tsdic(dic_):
    dic_['all'] = sum(dic_.values())
    d = sorted(dic_.items(),key=lambda item:item[1],reverse=True)
    d_={}
    for i in d:
        d_[i[0]]=i[1]
    s = json.dumps(d_,ensure_ascii=False)
    return s


def get_cate(content,dic,debug=False):

    count = {}
    name_count={}
    for name in dic:
        c = content.count(name)
        if c<=0 or name =='其他' or name=='其它':
            continue
        if debug:
            print(name,c)
        name_count[name]=c
        if dic[name] not in count:
            count[dic[name]]=0
        count[dic[name]]+= c

    return tsdic(name_count),tsdic(count)


def cucalute_one(id):
    try:
        print('get cate start')
        d = HomeCrawldata.get_by_id(id)
        d.product_name,d.industry = get_cate(d.content)
        d.save()
        print('get cate start')
    except:
        print('名称识别出错计算出错')


def update_all():
    name_to_cate = load()
    ll = HomeCrawldata.filter(industry__eq=None)

    for p in ll:
        n, c = get_cate(p.content,name_to_cate)
        p.industry = c
        p.product_name = n
        p.save()

    ll = HomeCrawldata.filter(industry__eq='')

    for p in ll:
        n, c = get_cate(p.content,name_to_cate)
        p.industry = c
        p.product_name = n
        p.save()


if __name__ =='__main__':

    update_all()














