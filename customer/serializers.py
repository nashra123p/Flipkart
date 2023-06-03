from rest_framework import serializers
from customer.models import *

class GetCustomerSerializers(serializers.ModelSerializer):
     
     class Meta:
          model = Customers
          fields="__all__"

class GetCustomerAddressSerializers(serializers.ModelSerializer):
     
     class Meta:
          model = Customers
          fields="__all__"


class CustomerDetailsAddressSerializers(serializers.ModelSerializer):
     customer_addresses = GetCustomerAddressSerializers(many=True)
     class Meta:
      model = Customers
      field=('first_name','last_name','city','pincode','dob'),
