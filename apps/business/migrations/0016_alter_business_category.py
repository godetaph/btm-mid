# Generated by Django 3.2.4 on 2021-06-23 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0015_auto_20210623_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_categories', to='business.category'),
        ),
    ]
