# Generated by Django 2.0.7 on 2018-09-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_requirments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=2, max_length=600),
            preserve_default=False,
        ),
    ]
