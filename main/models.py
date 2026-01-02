from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class OrgScale(models.Model):
    team_members = models.IntegerField()
    active_researchers = models.IntegerField()
    regional_chapters = models.IntegerField()
    schools_connected = models.IntegerField()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='posters/')
    text = RichTextField()
    
    def __str__(self):
        return self.title

class TeamMember(models.Model):
    image = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    description = models.TextField()
    added = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.role} - {self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Request(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    region = models.CharField(max_length=50)
    organization = models.CharField(max_length=200)
    purpose = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


        
