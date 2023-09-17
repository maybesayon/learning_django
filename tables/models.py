from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    bio = models.TextField()


    def __str__(self) :
        return self.name
    

class Items(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    catagory = models.CharField(max_length=30)
    uses = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name