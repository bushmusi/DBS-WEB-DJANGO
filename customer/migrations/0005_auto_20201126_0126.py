# Generated by Django 3.1.3 on 2020-11-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20201126_0008'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Temp',
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
    ]
