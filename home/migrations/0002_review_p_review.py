# Generated by Django 3.1.8 on 2021-12-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='p_review',
            field=models.TextField(null=True),
        ),
    ]
