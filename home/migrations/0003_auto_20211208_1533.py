# Generated by Django 3.2.8 on 2021-12-08 14:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_profile',
            name='about_klef',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='blog_profile',
            name='privay',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
