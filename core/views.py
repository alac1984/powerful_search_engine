from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models as m


def index_view(request):
    return render(request, 'core/index.html')


def search_view(request):
    posts = m.Post.objects.all()
    query = request.GET.get('q')
    page_num = request.GET.get('page')

    paginator = Paginator(posts.annotate(
        search=SearchVector('post_title', 'post_subtitle'),
    ).filter(search=query).order_by('post_title'), 15)

    num_results = paginator.count
    num_pages = paginator.num_pages

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        page_num = 1
        posts = paginator.page(page_num)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'num_results': num_results,
        'num_pages': num_pages,
        'page_range': paginator.page_range,
    }

    return render(request, 'core/search.html', context)


def detail_view(request, pk):
    return render(request, 'core/detail.html', {'pk': pk})

