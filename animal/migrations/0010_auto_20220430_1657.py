# Generated by Django 3.1 on 2022-04-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0009_auto_20220427_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hangqing',
            name='zuori',
            field=models.CharField(max_length=255, verbose_name='较昨天'),
        ),
    ]
