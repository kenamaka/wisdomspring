from django.db import models
from datetime import datetime

# Create your models here.

CATIGORIES = (
    ('Early Years','Early Years'),
    ('primary', 'Primary'),
    ('news letter','News Letter'),
    ('activities','Activities'),
    ('parent teachers forum ','Parent Teachers Forum'),
)

POSITION = (
    ('Teacher','Teacher'),
    ('Front Desk', 'Front Desk'),
    ('Cashier','Cashier'),
    ('Care Unit','Care Unit'),
    ('Security ','Security'),
    ('Nanny ','Nanny'),
    ('Others ','Others'),
)

DEPARTMENT = (
    ('Early Years','Early Years'),
    ('Primary', 'Primary'),
    ('Secondary ','Secondary'),
    ('ICT','ICT'),
    ('Music','Music'),
    ('Others ','Others'),
)
class posts(models.Model):
    title = models.CharField(max_length = 200)
    category = models.CharField(max_length=100, choices=CATIGORIES, default='green')
    snipet = models.CharField (max_length = 800, null= True, blank= True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'post/images', null = True, blank = True)
    create_time = models.DateTimeField(default = datetime.now, blank = True)

    class Meta:
        verbose_name_plural = "posts"
        ordering = ['-create_time',]
 
    def __str__(self):
        return self.title

class events(models.Model):
    title = models.CharField(max_length = 200)
    snipet = models.CharField (max_length = 800, null = True, blank = True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'post/images', null = True, blank = True)
    create_time = models.DateTimeField(default = datetime.now, blank = True)

    class Meta:
        verbose_name_plural = "events"
        ordering = ['-create_time',]
 
    def __str__(self):
        return self.title
        

class users(models.Model):
    first_name = models.CharField(max_length = 64)
    second_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    email = models.CharField(max_length = 64, null= True, blank = True)
    about = models.TextField()
    create_time = models.DateTimeField(default = datetime.now, blank = True)
    image = models.ImageField(upload_to = 'post/user_images', null = True, blank = True) 
   
    
    class Meta:
        verbose_name_plural = "users"
        ordering = ['-create_time',]

    def __str__(self):
        return self.username

class comments(models.Model) :
    fullname = models.CharField( max_length = 64)
    subject = models.CharField(max_length = 64 )
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length = 64, null= True, blank = True)
    message = models.TextField()
    create_time = models.DateTimeField(default = datetime.now, blank = True)

    class Meta:
        verbose_name_plural = "comments"
        ordering = ['-create_time',]
    
    def __str__(self):
        return self.fullname

class userapply(models.Model):
    first_name = models.CharField(max_length = 64)
    second_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length = 64, null= True, blank = True)
    position = models.CharField(max_length=100, choices=POSITION, default='Teacher',null = True, blank = True)
    department = models.CharField(max_length=100, choices=DEPARTMENT, default='Early Years',null = True, blank = True)
    about = models.TextField()
    create_time = models.DateTimeField(default = datetime.now, blank = True)
    image = models.ImageField(upload_to = 'post/user_images', null = True, blank = True) 
    pdf = models.FileField (upload_to = 'post/user_cv', null = True, blank = True)

    class Meta:
        verbose_name_plural = "userapply"
        ordering = ['-create_time',]
    
    def __str__(self):
        return self.username
