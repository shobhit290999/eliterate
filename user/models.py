from django.db import models

# Create your models here.
class UserAdd(models.Model):
    email  = models.EmailField(unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=30,null=True)
    pic = models.ImageField(upload_to="static/images/oio") #upload the images given by user in this path
    def __str__(self):
        return f"{self.email}"    


class Rejistermodal(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    cources = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.name   


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name        

#create table tablename(attr_name data_type(range))