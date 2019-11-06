from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django_dropbox_storage.storage import DropboxStorage
DROPBOX_STORAGE = DropboxStorage()
class App(models.Model):
    name = models.CharField(max_length=50)
    images = models.FileField(upload_to='images',storage=DROPBOX_STORAGE,blank=True)
    apkfile = models.FileField(upload_to='apks',storage=DROPBOX_STORAGE,blank=True)
    countryCode = models.CharField(max_length=50,null=True,blank=True)
    how = models.CharField(max_length=50,null=True,blank=True)
    addnl = models.CharField(max_length=100,null=True,blank=True)
    method = models.CharField(max_length=100,null=True,blank=True)
    appbuilder = models.CharField(max_length=100,null=True,blank=True)
    published = models.CharField(max_length=100,null=True,blank=True)
    apppub = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    verified = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='owner', null=True, blank=True, on_delete=models.SET_NULL)
    shortdesc = models.CharField(max_length=500,null=True,blank=True)
    longdesc = models.CharField(max_length=1000,null=True,blank=True)
    privpolicy = models.CharField(max_length=1000,null=True,blank=True)
    promovideo = models.CharField(max_length=150,null=True,blank=True)
    def __str__(self):
        return(self.name)
    

    

