# Generated by Django 2.2.5 on 2020-07-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20200701_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, related_name='lists', to='rooms.Room'),
        ),
    ]
