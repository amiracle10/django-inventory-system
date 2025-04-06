from django.urls import path
from inventorySystemApp import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('discussions/', views.discussions, name='discussions'),
    path('questions/', views.questions, name='questions'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('receiving/', views.receiving_items, name='Receiving'),
    # path('inventory/', views.inventory_management, name='Inventory_Management'),
    path('outbound/', views.send_items, name='Outbound'),
    path('dashboard/', views.dashboard, name = 'Dashboard'),

    path('discussions/', views.discussions, name='discussions'),
    path('discussions/<int:id>/', views.discussion_detail, name='discussion_detail'),
    path('discussions/create/', views.discussion_create, name='discussion_create'),
    path('discussions/delete/<int:id>/', views.discussion_delete, name='discussion_delete')

]
