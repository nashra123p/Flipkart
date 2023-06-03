from django.shortcuts import render
from customer.models import *
from customer.serializers import *

#create your views here.
from rest_framework   import  status
from rest_framework .views import  APIView
from rest_framework.response import Response

class GetCustomerView(APIView):
    def get(self,request):
        instance = Customers.objects.all()
        print("instance",instance)
        ser = GetCustomerSerializers(instance,many=True)
        print("ser",ser.data)
        return Response(ser.data)
    
    def post(self,request):
       params=request.data
       print("data",params)
       serl=GetCustomerSerializers(data=params)
       serl.is_valid(raise_exception=True)
       serl.save()
       return Response({"Message":"Save Successfully"})
    
class CustomerAddressView(APIView):
    def get(self,request):
        instance=CustomerAddress.objects.all()
        print("instance",instance)
        ser = GetCustomerAddressSerializers(instance,many=True)
        return Response(serializers.data)
class CustomerDetailsAddressView(APIView):

    def get(self,request,pk):
        instance=Customers.objects.filter(id=pk)
        ser =CustomerDetailsAddressSerializers(instance,many=True)
        return Response(ser.data)



                         

