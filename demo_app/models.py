from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class detail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username +": " + self.message