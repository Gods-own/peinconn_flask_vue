from flask import url_for

def get_pagination_info(request):
    page = request.args.get('page')

    per_page = request.args.get('per_page')

    max_per_page =  12

    if page is not None:
        page = int(page)
    else:
        page = 1    

    if per_page is None:
        per_page = 10
    else:
        if int(per_page) > max_per_page:
            per_page = 10   
        else:
            per_page = int(per_page) 

    return {'max_per_page': max_per_page, 'page': page, 'per_page': per_page}   

def get_pagination(endpoint, dbquery, **kwargs):
    try:
        links = {
            'firstPage': url_for(endpoint, **kwargs, page=dbquery.first, per_page=dbquery.per_page),
            'lastPage': url_for(endpoint, **kwargs, page=dbquery.last, per_page=dbquery.per_page),
            'prevPage': url_for(endpoint, **kwargs, page=dbquery.prev_num, per_page=dbquery.per_page),
            'nextPage': url_for(endpoint, **kwargs, page=dbquery.next_num, per_page=dbquery.per_page),
            'meta': {
                'paging': {
                'pageCount': dbquery.per_page,
                'totalPages': dbquery.pages,
                'totalItems': dbquery.total,
                'page': dbquery.page,
                'prev_page_num': dbquery.prev_num,
                'next_page_num': dbquery.next_num,
                'hasPrevPage': dbquery.has_prev,
                'hasNextPage': dbquery.has_next,
                }
            }
        }

        return links
    except Exception as e:
        return None    