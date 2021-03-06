# Generated by Django 2.2.10 on 2020-03-26 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avaluos', '0010_auto_20200324_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=255)),
                ('empresa', models.CharField(max_length=255)),
                ('rfc', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('correo', models.EmailField(blank=True, max_length=255, null=True)),
                ('contacto', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('estatus', models.BooleanField(default=True)),
                ('presidente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colegios_presidente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Colegios',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Valuador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(blank=True, max_length=255, null=True)),
                ('correo', models.EmailField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('celular', models.CharField(blank=True, max_length=255, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('estatus', models.BooleanField(default=True)),
                ('tipo', models.CharField(blank=True, choices=[('visita', 'Visita'), ('controlador', 'Controlador')], max_length=35, null=True)),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='valuadores', to='avaluos.Empresa')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='valuador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Valuadores',
            },
        ),
        migrations.CreateModel(
            name='PropuestaTecnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('archivo', models.FileField(upload_to='')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('respuesta', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('avaluo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propuesta_tecnica', to='avaluos.Avaluo')),
                ('responsable_carga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='valuador', to='avaluos.Valuador')),
            ],
            options={
                'verbose_name_plural': 'Propuestas Técnicas',
            },
        ),
        migrations.CreateModel(
            name='ColegioAvaluo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('avaluo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colegio_avaluo', to='avaluos.Avaluo')),
                ('colegio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='avaluos.Colegio')),
                ('evaluador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colegios', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Colegios',
            },
        ),
    ]
