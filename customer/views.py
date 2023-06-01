from django.shortcuts import render
from customer.models import *
from customer.serializers import *

#create your views here.
from rest_framework   import  status
from rest_framework .views import  APIView
from rest_framework.response import Response

class GetCustomersView(APIView):
    def get(self,request):
        instance = Customers.objects.all()
        print("instance",instance)
        serializer = GetCustomerSerializers(instance,many=True)
        return Response(serializer.data)
    def post(self,request):
       params=request.data
       print("data",params)
       serl=GetCustomerSerializers(data=params)
       serl.is_valid(raise_exception=True)
       serl.save()
       return Response({"Message":"Save Successfully"})
    
class CustomerDetailAddressView(APIView):

    def get(self,request,pk):
        instances=Customers.objects.filter(id=pk)
        serializer=CustomerDetailsAddressSerializers(instance,many=True)
        return=Response(ser.data)



                         

