import math
class Pager:
    pagesize = 8
    @classmethod
    def get_totalpages(self,totalcounts):
        return math.ceil(totalcounts*1.0/self.pagesize)

    @classmethod
    def get_pagecontext(self,context,totalCounts,currentPage):

        context['totalCounts'] = totalCounts
        context['totalPages'] = Pager.get_totalpages(totalCounts)
        currentPage = int(currentPage)
        if currentPage > context['totalPages']:
            currentPage = 1
        context['currentPage'] = currentPage
        return context





