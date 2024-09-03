from django.db import models
from account.models import CustomerDetails
from adminapp.models import AddRoom

# Create your models here.

class Book(models.Model):
    checkin= models.DateField()
    checkout=models.DateField()
    amount=models.FloatField()
    customer= models.ForeignKey(to=CustomerDetails,on_delete=models.CASCADE)
    room= models.ForeignKey(to=AddRoom,on_delete=models.CASCADE)