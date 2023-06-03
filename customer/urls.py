from django.urls import path,include
from customer.views import *
urlpatterns = [
   path('get-customers',GetCustomerView.as_view()),
     path('get-address',CustomerAddressView.as_view()),
]