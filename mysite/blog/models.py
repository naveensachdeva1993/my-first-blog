from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title


    
class person(models.Model):
    shirt_size=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        )

    name=models.CharField(max_length=200)
    size=models.CharField(max_length=1, choices=shirt_size)
    
