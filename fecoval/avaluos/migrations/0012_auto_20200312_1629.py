# Generated by Django 2.2.10 on 2020-03-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaluos', '0011_auto_20200312_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoscliente',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datoscliente',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datoscliente',
            name='curp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datoscliente',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datoscliente',
            name='nss',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datoscliente',
            name='persona',
            field=models.CharField(blank=True, choices=[('F', 'Persona Física'), ('M', 'Persona Moral')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datoscliente',
            name='rfc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datoscliente',
            name='telefono',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mancomunado',
            name='celular',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mancomunado',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mancomunado',
            name='rfc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mancomunado',
            name='telefono',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
