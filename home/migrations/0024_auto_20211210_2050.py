# Generated by Django 3.1.8 on 2021-12-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_blog',
            name='photo1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='all_blog',
            name='photo2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='all_blog',
            name='photo3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='all_blog',
            name='photo4',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
