# Generated by Django 5.1.3 on 2024-12-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.URLField()),
                ('formation_date', models.CharField(max_length=10)),
                ('debut_date', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=255)),
                ('members', models.TextField()),
                ('hit_songs', models.CharField(max_length=255)),
                ('albums', models.TextField()),
                ('awards', models.TextField()),
            ],
        ),
    ]
