# Generated by Django 2.2.10 on 2020-03-12 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaluos', '0008_avaluo_localizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaluo',
            name='datos_cliente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='avaluos.DatosCliente'),
        ),
    ]
