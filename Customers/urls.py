from django.urls import  path
from . import views

urlpatterns = [
    path('add', views.addcustomer , name="index"),
    path('delete', views.removecustomer , name="index"),
    path('edit', views.editcustomer , name="index"),
    path('view', views.viewcustomer , name="index")
]