# Generated by Django 3.1.3 on 2020-12-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20201206_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='lat',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='longt',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
    ]