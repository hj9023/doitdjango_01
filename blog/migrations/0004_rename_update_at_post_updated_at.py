# Generated by Django 4.1 on 2023-10-10 14:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_rename_create_at_post_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="update_at",
            new_name="updated_at",
        ),
    ]
