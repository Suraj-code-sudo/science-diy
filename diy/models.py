from django.db import models
from django.contrib.auth.models import User


class Experiments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    exp_name = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False, null=False)
    difficulty = models.IntegerField(blank=False)
    subject = models.CharField(blank=False, max_length=100)
    image = models.ImageField(upload_to='images/')
    safety = models.TextField(blank=False)
    claps = models.IntegerField(null=True, blank=True,default=1)
    steps = models.TextField(blank=True)
    
    def __str__(self):
        return self.exp_name
    
    class Meta:
        order_with_respect_to = 'user'
