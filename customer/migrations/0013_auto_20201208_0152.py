# Generated by Django 3.1.3 on 2020-12-07 22:52

import customer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20201206_0318'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Venue',
        ),
        migrations.RemoveField(
            model_name='itempost',
            name='title',
        ),
        migrations.AlterField(
            model_name='picture',
            name='path_addr',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[customer.models.validate_image]),
        ),
    ]