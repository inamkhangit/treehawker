# Generated by Django 3.1.8 on 2021-12-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20211207_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden_collection',
            name='category',
            field=models.CharField(max_length=99, null=True),
        ),
    ]
