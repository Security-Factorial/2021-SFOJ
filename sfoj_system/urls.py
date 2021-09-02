from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'sfoj_system'

urlpatterns = [
    path('', views.index, name='index'), #config의 'sfoj_system/'이 추가된 후 이곳의 url이 추가됨
    path('login/', auth_views.LoginView.as_view(template_name='common:login'), name='login'),
    path('list/',views.list, name = 'list'),
    path('list/<int:board_index>/', views.detail, name = 'detail'),
    path('uploads/',views.uploads, name='uploads'),
    path('signup/',views.signup, name='signup'),
]