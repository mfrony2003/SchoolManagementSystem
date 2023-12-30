from django.db import models


from apps.users.models.models import CustomUser, Gender, Religion

# Create your models here.
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    dob= models.DateField(blank=True, null= True)
    religion= models.ForeignKey(Religion,on_delete=models.DO_NOTHING)       
    nid_number= models.CharField(max_length=250,blank=True, null= True)
    phone_personal= models.CharField(max_length=250,blank=True, null= True)
    phone_emergengy= models.CharField(max_length=250,blank=True, null= True)
    gender = models.ForeignKey(Gender,on_delete=models.DO_NOTHING)  
    active= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.admin.username
