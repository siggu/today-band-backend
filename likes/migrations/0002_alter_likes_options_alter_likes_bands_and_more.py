# Generated by Django 5.1.3 on 2024-12-14 16:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_remove_band_user'),
        ('likes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likes',
            options={'verbose_name_plural': 'likes'},
        ),
        migrations.AlterField(
            model_name='likes',
            name='bands',
            field=models.ManyToManyField(related_name='liked_by', to='bands.band'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
