# Generated by Django 3.2.9 on 2021-11-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_alter_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]