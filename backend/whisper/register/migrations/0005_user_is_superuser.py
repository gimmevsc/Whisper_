# Generated by Django 5.0.6 on 2024-06-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "register",
            "0004_remove_groupmessage_group_remove_groupmessage_author_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]