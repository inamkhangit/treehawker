# Generated by Django 3.1.8 on 2021-12-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_all_cart_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=99)),
                ('name', models.CharField(max_length=99)),
                ('order_id', models.CharField(max_length=99)),
                ('order_serial', models.CharField(max_length=99)),
                ('number', models.CharField(max_length=99)),
                ('transaction_id', models.CharField(max_length=99)),
            ],
        ),
    ]