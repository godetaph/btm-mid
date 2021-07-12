# Generated by Django 3.2.4 on 2021-07-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0026_auto_20210701_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='category',
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='business_categories', to='business.Category'),
        ),
    ]
