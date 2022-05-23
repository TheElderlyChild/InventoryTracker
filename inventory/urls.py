from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),

    path('items/', views.ItemListView.as_view(), name='items'),
    path('item/<uuid:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/create/', views.ItemCreate.as_view(), name='item-create'),
    path('item/<uuid:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('item/<uuid:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),

    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<uuid:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('location/create/', views.LocationCreate.as_view(), name='location-create'),
    path('location/<uuid:pk>/update/', views.LocationUpdate.as_view(), name='location-update'),
    path('location/<uuid:pk>/delete/', views.LocationDelete.as_view(), name='location-delete'),

    path('item/<uuid:pk>/assign/', views.assign_item, name='item-assign'),
]

