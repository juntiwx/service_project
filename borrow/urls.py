from django.urls import path
from borrow import views

urlpatterns = [
    path('', views.borrow_list, name='borrow_list'),
    path('borrow/<int:pk>/', views.borrow_detail, name='borrow_detail'),
    path('borrow/new/', views.borrow_create, name='borrow_create'),
    path('borrow/<int:pk>/edit/', views.borrow_update, name='borrow_update'),
    path('borrow/<int:pk>/delete/', views.borrow_delete, name='borrow_delete'),
]