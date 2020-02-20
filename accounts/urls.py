from django.urls import path
from . import views


# 경로 앱 이름 지정 'accounts:index 앱 name 역할을 한다.'
app_name = 'accounts'


# accounts/@@@
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
]

