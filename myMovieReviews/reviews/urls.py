from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='view_list'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/<int:pk>/edit/', views.review_edit, name='review_edit'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),
]