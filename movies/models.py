from django.db import models
from django.core.validators import MaxValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=200)
    picture = models.URLField(max_length=1000, default='https://images.app.goo.gl/99rMYE67Hjuc83bY6')
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    notes = models.TextField(max_length=2000, default='')

    def __str__(self):
        return self.name
