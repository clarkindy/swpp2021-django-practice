# Generated by Django 3.2.8 on 2021-10-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
