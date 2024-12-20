# Generated by Django 4.2.16 on 2024-11-09 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
        ('factura', '0002_alter_detallefactura_factura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.factura')),
            ],
        ),
        migrations.CreateModel(
            name='TipoNota',
            fields=[
                ('id_tipo_nota', models.AutoField(primary_key=True, serialize=False)),
                ('nom_nota', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoNota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(blank=True, null=True)),
                ('nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.nota')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
        ),
        migrations.AddField(
            model_name='nota',
            name='productos',
            field=models.ManyToManyField(through='notas.ProductoNota', to='producto.producto'),
        ),
        migrations.AddField(
            model_name='nota',
            name='tipo_nota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.tiponota'),
        ),
    ]
