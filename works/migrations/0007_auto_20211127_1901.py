# Generated by Django 3.2.9 on 2021-11-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed_project_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='pending_projects_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='satisfied_clients_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]