# Generated by Django 3.0.8 on 2022-03-20 16:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_auto_20220319_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yangzhiziliao',
            name='neirong',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='文章内容', verbose_name='文章内容'),
        ),
    ]
