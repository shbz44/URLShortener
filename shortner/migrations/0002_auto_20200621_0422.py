# Generated by Django 3.0.7 on 2020-06-20 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='user_id',
            new_name='user',
        ),
    ]
