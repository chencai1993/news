# -*- coding: utf-8 -*-



import json

def get_paramer(request):
    dic_ = {}
    try:
        dic_ = to_json(request)
    except:
        pass
    return dic_

def to_json(request):
    

    concat = request.POST
    dic_ = dict(concat)
    if len(dic_)==0:
        concat = request.GET
        dic_ = dict(concat)
    
    for key in dic_:
        if len(dic_[key])==1:
            dic_[key]=dic_[key][0]
    
    return dic_

    
        

