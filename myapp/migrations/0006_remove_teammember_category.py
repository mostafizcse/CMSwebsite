# Generated by Django 2.0.7 on 2018-08-30 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_teammember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='category',
        ),
    ]