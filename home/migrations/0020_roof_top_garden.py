# Generated by Django 3.1.8 on 2021-12-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_make_your_garden_yourself'),
    ]

    operations = [
        migrations.CreateModel(
            name='roof_top_garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=99)),
                ('name', models.CharField(max_length=99)),
                ('category', models.CharField(max_length=99, null=True)),
                ('price', models.CharField(max_length=99)),
                ('serial', models.CharField(max_length=99)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
            ],
        ),
    ]
