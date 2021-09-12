from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('search/<str:query>', views.search_view, name='search'),
    path('search/<str:query>/<int:pk>', views.detail_view, name='detail')
]
