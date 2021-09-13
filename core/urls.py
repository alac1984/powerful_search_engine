from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('search/', views.search_view, name='search'),
    path('search/results/<int:result_id>', views.detail_view, name='detail')
]
