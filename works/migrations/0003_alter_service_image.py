# Generated by Django 3.2.9 on 2021-11-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20211125_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='service/'),
        ),
    ]
