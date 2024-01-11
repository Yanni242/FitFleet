from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_rename_exercises_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.CharField(choices=[('Shoulders', 'Shoulders'), ('Arms', 'Arms'), ('Chest', 'Chest'), ('Back', 'Back'), ('Abs', 'Abs'), ('Legs', 'Legs')], max_length=20),
        ),
    ]
