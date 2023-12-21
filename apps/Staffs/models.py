from django.db import models


from apps.users.models.models import CustomUser, Gender

# Create your models here.
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.ForeignKey(Gender,on_delete=models.DO_NOTHING)  
    active= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.admin.username
