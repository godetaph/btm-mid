# Generated by Django 3.2.4 on 2021-07-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0031_alter_payment_paid_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscategory',
            name='append_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
