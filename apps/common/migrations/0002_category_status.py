# Generated by Django 5.1 on 2024-08-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[(0, 'Movie'), (1, 'News')], default=0),
        ),
    ]
