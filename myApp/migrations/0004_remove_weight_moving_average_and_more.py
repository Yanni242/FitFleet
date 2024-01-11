from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weight',
            name='moving_average',
        ),
        migrations.RemoveField(
            model_name='weight',
            name='weekly_rate',
        ),
    ]
