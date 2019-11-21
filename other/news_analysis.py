import cate,keywords,summary,date,check

def news_analysis(id):

    print('start analysis %s'%(id))
    cate.cucalute_one(id)
    keywords.cucalute_one(id)
    summary.cucalute_one(id)
    print('end analysis %s' % (id))

if __name__=='__main__':

    print('start analysis' )
    cate.update_all()
    keywords.update_all()
    summary.update_all()
    date.update_all()
    check.update_all()
    print('end analysis' )


