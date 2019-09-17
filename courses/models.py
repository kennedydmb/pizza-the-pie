from django.db import models
from django.db.models import Avg

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.name
        
