from django.contrib import admin
from .models import Bmi, Calorie, Weight, Exercise

class BmiAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'bmi', 'date')

class CalorieAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height', 'gender', 'activity_level', 'calorie_intake', 'date')

class WeightAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'notes', 'date')

admin.site.register(Exercise)
admin.site.register(Bmi, BmiAdmin)
admin.site.register(Calorie, CalorieAdmin)
admin.site.register(Weight, WeightAdmin)
