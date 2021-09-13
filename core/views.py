from django.shortcuts import render


def index_view(request):
    return render(request, 'core/index.html')


def search_view(request):
    if request.method == 'POST':
        query = request.POST['query']
        if query == "":
            return render(request, 'core/search.html', {'query': "You didn't search for anything"})
        else:
            return render(request, 'core/search.html', {'query': query})


def detail_view(request, query, pk):
    return render(request, 'core/detail.html', {'pk': pk})

