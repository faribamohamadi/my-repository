# Generated by Django 2.2.12 on 2021-07-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_slider_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(upload_to='public/images/sliders'),
        ),
    ]
