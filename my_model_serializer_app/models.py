from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    subject = models.CharField(max_length=100)
    details = models.TextField()
    def __str__(self):
        return self.name
    
