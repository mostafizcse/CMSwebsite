# Generated by Django 2.0.7 on 2018-09-08 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_menu',
            name='Example',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp.Example'),
            preserve_default=False,
        ),
    ]
