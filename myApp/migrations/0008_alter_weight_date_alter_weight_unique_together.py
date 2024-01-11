from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0007_alter_exercise_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterUniqueTogether(
            name='weight',
            unique_together={('user', 'date')},
        ),
    ]
