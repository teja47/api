# Generated by Django 3.1.1 on 2020-10-14 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('photos', models.ImageField(blank=True, upload_to='')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('awards', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('movies', models.TextField()),
                ('socialMedia', models.TextField()),
                ('age', models.IntegerField()),
                ('field', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('youtubeLink', models.TextField(blank=True)),
                ('contentHead', models.TextField(blank=True)),
                ('cast', models.TextField(blank=True, default='000')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('poster', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('links', models.TextField()),
            ],
        ),
    ]
