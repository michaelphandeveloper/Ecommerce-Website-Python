from django.urls import path
from . import views

urlpatterns = [
  path('', views.store, name='store'),
  path('cart/', views.cart, name="cart")
]