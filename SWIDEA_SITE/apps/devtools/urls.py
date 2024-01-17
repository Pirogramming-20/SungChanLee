from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
    path('list', devtools_list, name = 'list'),
    path('create/', devtool_create, name = 'create'),
    path('delete/<int:pk>/',devtool_delete,name = 'delete'),
    path('detail/<int:pk>/',devtool_detail, name = 'detail'),
    path('update/<int:pk>/', devtool_update, name = 'update'),
]