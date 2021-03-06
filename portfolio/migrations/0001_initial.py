# Generated by Django 4.0.1 on 2022-02-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=250)),
                ('image', models.ImageField(height_field='url_height', upload_to='portfolio/images/', width_field='url_width')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
