# Generated by Django 4.1 on 2023-10-09 13:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_update_at_alter_post_create_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="create_at",
            new_name="created_at",
        ),
    ]
