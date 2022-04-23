from django.db import models
from django.urls import reverse

from django.core.validators import MinLengthValidator

# Create your models here.


class Make(models.Model):
        name = models.CharField(
                max_length=200, 
                help_text='Enter a make (e.g. Dodge)',
                validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
                )
        
        def __str__(self):
                """String for representing the Model object."""
                return self.name
        
        def get_absolute_url(self):
                return reverse('gcbv:make_detail', args=[self.pk])


class Auto(models.Model):
        nickname = models.CharField(
                max_length=200,
                validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
                )
        mileage = models.PositiveIntegerField()
        comments = models.CharField(max_length=300)
        make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
        
        def __str__(self):
                """String for representing the Model object."""
                return self.nickname