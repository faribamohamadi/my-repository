# Generated by Django 2.2.12 on 2021-07-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210726_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(upload_to=' public/images/sliders'),
        ),
    ]
