from django.db import models
from datetime import datetime
# Create your models here.

class mysite(models.Model):
    username = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField()
    password = models.CharField(max_length=100,) 
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=datetime.now, editable=False)
    class Meta:
        db_table = "mysite"

class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title 
