from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
    class_choice = (
        ('t', 'Home Tution'),
        ('c', 'Coaching'),
        ('b', 'both')
    )
    teacher=models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    class_type = models.CharField(max_length=20, choices=class_choice)
    name = models.CharField('Your Name',max_length=120)
    institute_name = models.CharField('Institute Name',max_length=50,null=True)
    email = models.CharField('Enter Your E'
                             ''
                             ''
                             'mail',max_length=120)
    contact = models.IntegerField('Mobile Number')
    locality = models.CharField(max_length=50,default="optional")
    city = models.CharField('City',max_length=20)
    state = models.CharField('State',max_length=20)
    votes_total = models.IntegerField(default=1)
    acheivements = models.TextField(max_length=1000,help_text = 'Description about your Acheivements and Awards')
# address = models.ForeignKey('Location',on_delete=models.SET_NULL,null=True)
    experience = models.IntegerField('Years')
    videolinks = models.CharField('Notes Or Video Links',max_length=120)
    def __str__(self):
        return self.name

class Upvoter(models.Model):
    upvoted=models.ForeignKey(User, on_delete=models.CASCADE)
    upvoter = models.CharField('Upvoter',max_length=40,default="None")
    def __str__(self):
        return str(self.upvoted) + self.upvoter

class Create(models.Model):
    creater=models.ForeignKey(User, on_delete=models.CASCADE)
    choices1 = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','other')
        )


    class_name = models.CharField(max_length=10,choices=choices1)
    subject = models.CharField('Subject',max_length=40)

    def __str__(self):
        return self.class_name+self.subject

class Payment(models.Model):
    premium = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.transaction_id
