from django.db import models
from courses.models import Course
from django.utils import timezone
import datetime

# Create your models here.
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    course = models.ForeignKey(Course)
    pub_date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100)
    comment = models.TextField(max_length=300)
    rating = models.IntegerField(choices=RATING_CHOICES)