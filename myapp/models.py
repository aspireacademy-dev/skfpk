from django.db import models

# Create your models here.

class Header(models.Model):
    h1=models.CharField(max_length=4000)
    description=models.TextField()
    background_image=models.ImageField(upload_to="pics",default="")
def __str__(self):
    return self.h1+self.description+self.background_image
class headerbox(models.Model):
    box_h1 = models.CharField(max_length=4000)
    box_description = models.TextField()
def __str__(self):
    return self.box1_h1+self.box1_description

class Before_Footer_Upcoming_Events(models.Model):
    hdeading=models.CharField(max_length=400)
    e_description=models.TextField()
    box_h2=models.CharField(max_length=400)
    box_description2=models.TextField()
    box_image=models.ImageField(upload_to="events",default="")
def __str__(self):
    return  self.heading+self.e_description+self.box_h2+self.box_description2+self.box_image

class contact(models.Model):
      fname=models.CharField(max_length=400)
      lname=models.CharField(max_length=400)
def __str__(self):
    return self.fname+self.lname
class contacttest(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=50)
def __str__(self):
    return self.firstname+self.lastname

class contactlast(models.Model):
     firstname1=models.CharField(max_length=40)
     lastname1=models.CharField(max_length=40)
def __str__(self):
    return self.firstname1+self.lastname1

