from django.db import models

class Person(models.Model):
    
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    #creation_date = models.DateTimeField('date registered')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.username
