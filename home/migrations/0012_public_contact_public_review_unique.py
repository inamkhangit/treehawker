# Generated by Django 3.1.8 on 2021-12-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20211207_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='public_contact',
            name='public_review_unique',
            field=models.CharField(max_length=99, null=True),
        ),
    ]
