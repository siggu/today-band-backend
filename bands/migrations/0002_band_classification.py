# Generated by Django 5.1.3 on 2024-12-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='classification',
            field=models.CharField(choices=[('ga', '가'), ('na', '나'), ('da', '다'), ('ra', '라'), ('ma', '마'), ('ba', '바'), ('sa', '사'), ('ah', '아'), ('ja', '자'), ('cha', '차'), ('ka', '카'), ('ta', '타'), ('pa', '파'), ('ha', '하')], default='ga', max_length=3),
        ),
    ]
