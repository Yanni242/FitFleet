from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_remove_weight_moving_average_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Shoulders', 'Shoulders'), ('Arms', 'Arms'), ('Chest', 'Chest'), ('Abs', 'Abs'), ('Legs', 'Legs')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tips', models.TextField()),
                ('video_url', models.URLField()),
            ],
        ),
    ]
