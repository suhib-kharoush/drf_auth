from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.

class Maintenance(models.Model):
    car_model = models.CharField(max_length=64)
    problem_description = models.TextField()
    technician = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    deliver_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_model
