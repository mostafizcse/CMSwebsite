# Generated by Django 2.0.7 on 2018-09-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20180830_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='')),
                ('tital', models.CharField(max_length=300)),
                ('subtitl', models.CharField(max_length=300)),
            ],
        ),
    ]