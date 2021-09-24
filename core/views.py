from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, SearchRank, TrigramSimilarity
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models as m


def return_numbers_for_paginator(num_pages, page):
    """"
    A function that gives the 5 numbers to be showed in search paginator
    """
    values = [n + 1 for n in range(num_pages)][:5]
    return values if page in values else [n + page - 5 for n in values]


def index_view(request):
    return render(request, 'core/index.html')


def search_view(request):
    posts = m.Post.objects.all()
    query = request.GET.get('q')
    page_num = request.GET.get('page')

    if query is None:
        return HttpResponseRedirect(reverse('core:index'))

    search_query = SearchQuery(query, config='english')

    paginator = Paginator(
        posts.annotate(
            rank=SearchRank(F('vector_column'), search_query) + TrigramSimilarity('post_title', query)
        ).filter(rank__gte=0.15).order_by('-rank'), 15
    )

    num_results = paginator.count
    num_pages = paginator.num_pages

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        page_num = 1
        posts = paginator.page(page_num)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Numbers for paginator
    num_paginator = return_numbers_for_paginator(num_pages, int(page_num))

    context = {
        'posts': posts,
        'num_results': num_results,
        'num_pages': num_pages,
        'num_paginator': num_paginator,
        'first_num_paginator': num_paginator[0],
        'last_num_paginator': num_paginator[-1]
    }

    return render(request, 'core/search.html', context)


def detail_view(request, pk):
    return render(request, 'core/detail.html', {'pk': pk})

