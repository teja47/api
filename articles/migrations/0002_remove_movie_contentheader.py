# Generated by Django 3.1.1 on 2020-10-02 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='contentHeader',
        ),
    ]
