# Generated by Django 3.1.1 on 2020-10-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20201025_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='poster',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]