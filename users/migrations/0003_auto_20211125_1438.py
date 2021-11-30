# Generated by Django 3.2.9 on 2021-11-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_id',
            field=models.AutoField( primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
