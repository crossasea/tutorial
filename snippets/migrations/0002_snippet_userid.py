# Generated by Django 4.1.1 on 2022-10-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]
