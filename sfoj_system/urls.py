from django.urls import path

from . import views

app_name = 'sfoj_system'

urlpatterns = [
    path('', views.index, name='index'), #config의 'sfoj_system/'이 추가된 후 이곳의 url이 추가됨
    path('list/',views.list, name = 'list'),
    path('list/<int:board_index>/', views.detail, name = 'detail'),
    path('uploads/',views.uploads, name='uploads'),
]