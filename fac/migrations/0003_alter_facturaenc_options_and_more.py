# Generated by Django 5.1 on 2024-11-04 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0002_facturaenc_facturadet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturaenc',
            options={'verbose_name': 'Encabezado Factura', 'verbose_name_plural': 'Encabezado Facturas'},
        ),
        migrations.RenameField(
            model_name='facturaenc',
            old_name='Cliente',
            new_name='cliente',
        ),
    ]