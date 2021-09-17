from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path(r'', views.index_view, name='index'),
    path(r'search/', views.search_view, name='search'),
    path(r'search/results/<int:pk>', views.detail_view, name='detail')
]
