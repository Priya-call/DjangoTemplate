# Generated by Django 3.0.8 on 2021-05-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0002_customermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
                ('order', models.CharField(max_length=10)),
                ('orderitem', models.CharField(max_length=10)),
            ],
        ),
    ]
