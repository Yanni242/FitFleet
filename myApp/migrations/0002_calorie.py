from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('activity_level', models.CharField(choices=[('S', 'Sedentary: little or no exercise'), ('L', 'Light: exercise 1-3 times per week'), ('M', 'Moderate: exercise 4-5 times per week'), ('A', 'Active: daily exercise or intense exercise 3-4 times per week'), ('V', 'Very Active: intense exercise 6-7 times per week'), ('E', 'Extra Active: very intense exercise daily or physical job')], max_length=1)),
                ('calorie_intake', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
