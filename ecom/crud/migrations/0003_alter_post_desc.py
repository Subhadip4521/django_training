# Generated by Django 4.1.5 on 2023-02-01 11:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0002_rename_image_post_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="desc",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
