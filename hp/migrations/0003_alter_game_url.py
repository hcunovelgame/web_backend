# Generated by Django 3.2 on 2021-06-18 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0002_auto_20210618_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
