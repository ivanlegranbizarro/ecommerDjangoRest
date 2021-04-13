from django.urls import path
from orders import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrderList.as_view()),
]
