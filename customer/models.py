from django.db import models



class Customers(models.Model):
    first_name=models.CharField(max_length=15,null=True,blank=True)
    last_name=models.CharField(max_length=15,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)


    def __str__(self) :
        return str(self.first_name)
    
class CustomerAddress(models.Model):
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,blank=True,related_name="customer_addresses")
    street_name=models.CharField(max_length=15,null=True,blank=True)
    street_number=models.IntegerField(null=True,blank=True)
    city=models.CharField(max_length=15,null=True,blank=True)
    country=models.CharField(max_length=15,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)

    def __self__(self) :
        return str(self.street_name)
    
    class Customer_Addhar(models.Model):
        customer=models.OneToOneField(Customers,on_delete=models.CASCADE,null=True,blank=True)
        addhar_number=models.IntegerField(null=True,blank=True)
        addhar_name=models.CharField(max_length=15,null=True,blank=True)
    def _self_(self):
        return self.addhar_name
        
        
        
    



