# Generated by Django 3.1.1 on 2020-10-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20201002_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='ch',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='contentHeader',
            field=models.CharField(max_length=120),
        ),
    ]
