# Generated by Django 3.1.8 on 2021-12-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_garder_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='fruit_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('price', models.CharField(max_length=99)),
                ('serial', models.CharField(max_length=99)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
            ],
        ),
    ]
