from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_exercises'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exercises',
            new_name='Exercise',
        ),
    ]
