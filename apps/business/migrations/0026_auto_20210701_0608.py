# Generated by Django 3.2.4 on 2021-07-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0025_alter_business_gross_sale_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='capitalization_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='gps_accuracy',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='gps_altitude',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='gps_lattitude',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='gps_longitude',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='total_employees',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='total_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='total_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
