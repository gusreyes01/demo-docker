# Generated by Django 2.2.10 on 2020-03-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaluos', '0007_auto_20200311_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaluo',
            name='localizado',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=35, null=True),
        ),
    ]