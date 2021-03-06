# Generated by Django 2.0.7 on 2018-09-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_featuretitle_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=225)),
                ('message', models.TextField()),
                ('timestrimp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
