from django.urls import path
from inventorySystemApp import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('topics/', views.topics, name='topics'),
    path('questions/', views.questions, name='questions'),
    path('about/', views.about, name='about'),
    path('receiving/', views.receiving_items, name='Receiving'),
    # path('inventory/', views.inventory_management, name='Inventory_Management'),
    path('outbound/', views.send_items, name='Outbound'),
    path('dashboard/', views.dashboard, name = 'Dashboard')
]
