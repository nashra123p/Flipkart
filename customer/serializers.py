from rest_framework import serializers
from customer.models import *

class GetCustomerSerializers(serializers.ModelSerializer):
     
     class Meta:
          model = Customers
          fields="__all__"

class GetCustomerSerializers(serializers.ModelSerializer):
     
     class Meta:
          model = Customers
          fields="__all__"


class CustomerDetailsAddressSerializers(serializers.ModelSerializer):
     customer_addresses = GetAddressSerializers(many=True)
     class Meta:
      model = Customers
      field=('first_name','last_name','city','pincode','dob'),
