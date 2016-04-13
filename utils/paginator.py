#coding:utf-8
from django.core.paginator import Paginator

#创建一个通用的翻页数据结构获取接口
#objs:对象
#cnt_per_page:每页显示的个数
#half_show_length:翻页部分的左右各有多少个
def paginator_queryset(objs,page_no,cnt_per_page=10,half_show_length=5):
    p = Paginator(objs,cnt_per_page)
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no <= 0:
        page_no = 1

    page_links = [i for i in range(page_no-half_show_length,page_no+half_show_length+1) if i>0 and i<=p.num_pages]

    page = p.page(page_no)
    previous_link = page_links[0]-1
    next_link = page_links[-1]+1
    pagination_data = {'has_previous':previous_link>0,"has_next":next_link<=p.num_pages,"previous_link":previous_link,"next_link":next_link,"page_cnt":p.num_pages,"current_no":page_no,"page_links":page_links}

    return (page.object_list,pagination_data)
