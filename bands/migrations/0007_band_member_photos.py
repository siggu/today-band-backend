# Generated by Django 5.1.3 on 2024-12-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0006_alter_band_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='member_photos',
            field=models.TextField(null=True),
        ),
    ]
