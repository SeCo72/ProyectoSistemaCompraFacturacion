# Generated by Django 5.1 on 2024-11-04 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0003_alter_facturaenc_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturadet',
            options={'permissions': [('sup_caja_facturadet', 'Permisos de Supervisor de Caja Detalle')], 'verbose_name': 'Detalle Factura', 'verbose_name_plural': 'Detalles Facturas'},
        ),
        migrations.AlterModelOptions(
            name='facturaenc',
            options={'permissions': [('sup_caja_facturaenc', 'Permisos de Supervisor de Caja Encabezado')], 'verbose_name': 'Encabezado Factura', 'verbose_name_plural': 'Encabezado Facturas'},
        ),
    ]