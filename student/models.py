from django.db import models


class Support(models.Model):
    name= models.CharField(max_length=20)
    email = models.EmailField(verbose_name='email-id')
    message =models.TextField(max_length=100,verbose_name='How can we help?')

    def __str__(self):
        return str(self.name)






