from django.urls import path
from . import views

urlpatterns = [

    
    path('signin/',views.signin),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='logout'),


    path('', views.index),
    path('clients/', views.clients, name='clients'),

    path('clients/delete/<uuid:id>', views.deleteclient, name='deleteclient'),  
    path('clients/update/<uuid:id>/', views.updateclient, name='updateclient'),

    path('vehicles/',views.vehicles),

    path('vehicles/delete/<uuid:id>', views.deletevehicle, name='deletevehicle'),  
    path('vehicles/update/<uuid:id>/', views.updatevehicle, name='updatevehicle'),

    path('services/',views.services),

    path('services/delete/<uuid:id>', views.deleteservice, name='deleteservice'),  
    path('services/update/<uuid:id>/', views.updateservice, name='updateservice'),

    path('services/get_owner/<uuid:id>', views.get_owner, name='get_owner'),
    path('services/get_cost/<uuid:id>', views.get_cost, name='get_cost'),

    path('billing/',views.billing),

    path('billing/<uuid:id>',views.make_billing),
    path('billing/delete/<uuid:id>', views.deletebilling, name='deletebilling'),  
    path('billing/update/<uuid:id>/', views.updatebilling, name='updatebilling'),


    path('billing/get_owner/<uuid:id>', views.get_owner, name='get_owner'),
    path('billing/get_cost/<uuid:id>', views.get_cost, name='get_cost'),
]