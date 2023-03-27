from django.urls import path
from . import views

urlpatterns = [
    path('quote', views.quote, name='quote'),
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_quote, name='add_to_quote'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]