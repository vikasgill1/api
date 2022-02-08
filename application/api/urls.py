import imp
from django.urls import path
from .views import *


urlpatterns = [
    path('register/',RegisterViewApi.as_view(),name='register'),
    path('signup/',SignUpApi.as_view(),name='register'),
    path('login/',LoginApiView.as_view(),name='register'),
    path('Updateuser/<str:pk>/',UpdateApi,name='register'),
    path('deleteuser/<str:pk>/',DeleteApi.as_view(),name='register'),
    path('list/',product_list,name='register'),
    path('search/<str:pk>/',product_search,name='register'),
    path('crete/',product_create,name='register'),
    path('update/<str:pk>/',product_update,name='register'),
    path('delete/<str:pk>/',product_delete,name='register'),
]
