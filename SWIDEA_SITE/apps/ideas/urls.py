from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('', ideas_list, name = 'list'),
    path('create/', ideas_create, name = 'create'),
    path('detail/<int:pk>/', idea_detail , name = 'detail'),
    path('delete/<int:pk>/',idea_delete, name = 'delete'),
    path('update/<int:pk>/', idea_update, name = 'update'),
]