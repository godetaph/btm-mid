# Generated by Django 3.2.4 on 2021-07-18 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0046_auto_20210717_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='picture4',
        ),
        migrations.RemoveField(
            model_name='business',
            name='picture5',
        ),
        migrations.RemoveField(
            model_name='business',
            name='picture6',
        ),
    ]
