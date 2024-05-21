from django.db import models

# Create your models here.

class ElaClass(models.Model):
    cName = models.CharField(max_length=50)
    mMembers = models.IntegerField()
    maxMembers = models.IntegerField()    

    def __str__(self):
        return self.cName


class SocialClass(models.Model):
    cName = models.CharField(max_length=50)
    mMembers = models.IntegerField()
    maxMembers = models.IntegerField()    

    def __str__(self):
        return self.cName



class ScienceClass(models.Model):
    cName = models.CharField(max_length=50)
    mMembers = models.IntegerField()
    maxMembers = models.IntegerField()    

    def __str__(self):
        return self.cName



class MathClass(models.Model):
    cName = models.CharField(max_length=50)
    mMembers = models.IntegerField()
    maxMembers = models.IntegerField()    

    def __str__(self):
        return self.cName

