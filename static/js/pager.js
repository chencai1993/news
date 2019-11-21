 isFirst = true

function load_pager(totalPages,totalCounts,currentPage)
{
    $.jqPaginator('#pagination', {
            totalPages: totalPages,
            visiblePages: 10,
            totalCounts:totalCounts,
            currentPage: currentPage,
            onPageChange: function (num, type) {
                    if(isFirst){
                        isFirst = false;
                    }
                    else
                    {
                        $("[name='currentPage']").val(num);
                        $('form').submit();
                    }
            }
            });
}

