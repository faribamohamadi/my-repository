# Generated by Django 2.2.12 on 2021-07-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='name',
        ),
    ]
