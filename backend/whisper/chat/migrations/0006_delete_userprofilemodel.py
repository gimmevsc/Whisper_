# Generated by Django 5.0.6 on 2024-06-23 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_remove_groupmessage_group_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileModel',
        ),
    ]
