# Generated by Django 3.2.4 on 2021-06-23 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0016_alter_business_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_business', to=settings.AUTH_USER_MODEL),
        ),
    ]
