# Generated by Django 4.1.3 on 2022-12-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('img', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
