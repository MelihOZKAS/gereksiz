# Generated by Django 4.2.7 on 2023-12-02 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_image_post_resim"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="small_banner", new_name="editor",
        ),
    ]
