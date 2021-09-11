from django.db import models
from datetime import time
# Create your models here.
class mydata(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=time(9))
    phoneno = models.IntegerField(default=0000000)
    reason = models.CharField(max_length=400 , default="q")
    email = models.CharField(max_length=50 , default="no email")
    
    def __str__(self):
        return f"{self.title}: date{self.date} phoneno {self.phoneno} reason {self.reason}"


