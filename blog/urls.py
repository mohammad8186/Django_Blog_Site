from django.urls import path
from . import views

urlpatterns = [
    path('' ,  views.home , name = 'home'),
    path('post-list', views.post_list, name='post_list'),
    path('post/<uuid:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<uuid:id>/edit/', views.post_update, name='post_update'),
    path('post/<uuid:id>/delete/', views.post_delete, name='post_delete'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
