from django.db import models
from courses.models import Course
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    course = models.ForeignKey(Course, default="course")
    pub_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user_name = models.CharField(max_length=100, blank=True)
    comment = models.TextField(max_length=300, blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=False)