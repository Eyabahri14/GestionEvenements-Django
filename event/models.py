from django.db import models
from django.utils import timezone

from django.core.exceptions import ValidationError
from datetime import datetime
# Create your models here


def is_date_event(value):
    if value <= timezone.now():
        raise ValidationError(
            'event date must be greater than the current date')
    return value


class Event(models.Model):

    category_list = (
        ("Musique", "Musique"),
        ("Sport", "Sport"),
        ("Cinema", "Cinema")
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(null=True)
    categoy = models.CharField(choices=category_list, max_length=10)
    state = models.BooleanField(default=False)
    nbr_participant = models.IntegerField(default=0)
    evt_date = models.DateTimeField(null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    evt_date__gte=datetime.now()
                ),
                name='Please check out the event date'
            ),
        ]
