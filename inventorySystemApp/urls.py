from django.urls import path
from inventorySystemApp import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('discussions/', views.discussions, name='discussions'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('topics/', views.topics, name='topics'),
    # path('inventory/', views.inventory_management, name='Inventory_Management'),
    # path('outbound/', views.send_items, name='Outbound'),
    # path('dashboard/', views.dashboard, name = 'Dashboard'),

    # path('discussions/', views.discussions, name='discussions'),
    # path('discussions/<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),
    path('discussions/<int:pk>/', views.discussion_detail, name='discussion_detail'),
    path('discussions/create/', views.discussion_create, name='discussion_create'),
    path('discussions/create/<int:pk>/', views.discussion_create, name='discussion_create'),
    path('discussions/delete/<int:id>/', views.delete_discussion, name='delete_discussion'),
    path('comments/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
   

]


