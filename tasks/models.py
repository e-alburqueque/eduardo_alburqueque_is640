from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=20,null=False)
    description = models.TextField(max_length=200, default = "")
    is_done = models.BooleanField(default=False)

#check contact
class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    email = models.EmailField(unique=True) 
    notes = models.TextField(max_length=200, default="Write Notes Here....")
    created_time = models.DateTimeField(auto_now_add=True)

def get_absolute_url(self):
        return reverse('contact_detail', kwargs={'pk': self.pk})