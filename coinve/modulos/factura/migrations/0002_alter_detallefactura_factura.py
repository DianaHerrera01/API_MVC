# Generated by Django 4.2.16 on 2024-10-30 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='factura.factura'),
        ),
    ]
