from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Bmi(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateField(auto_now_add = True)

class Calorie(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    ACTIVITY_LEVEL_CHOICES = (
        ('S', 'Sedentary: little or no exercise'),
        ('L', 'Light: exercise 1-3 times per week'),
        ('M', 'Moderate: exercise 4-5 times per week'),
        ('A', 'Active: daily exercise or intense exercise 3-4 times per week'),
        ('V', 'Very Active: intense exercise 6-7 times per week'),
        ('E', 'Extra Active: very intense exercise daily or physical job'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    activity_level = models.CharField(max_length = 1, choices = ACTIVITY_LEVEL_CHOICES)
    calorie_intake = models.FloatField()
    date = models.DateField(auto_now_add = True)

class Weight(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    weight = models.FloatField()
    notes = models.TextField(blank = True, null = True)
    date = models.DateField()

    class Meta:
        unique_together = ('user', 'date')

class Exercise(models.Model):
    CATEGORY_CHOICES = [
        ('Shoulders', 'Shoulders'),
        ('Arms', 'Arms'),
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Abs', 'Abs'),
        ('Legs', 'Legs')
    ]

    category = models.CharField(max_length = 20, choices = CATEGORY_CHOICES)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    tips = models.TextField()
    video_url = models.URLField()
    
    def __str__(self):
        return self.name

