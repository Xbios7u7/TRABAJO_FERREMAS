# Generated by Django 4.2.1 on 2024-05-19 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cargo', models.CharField(default='Desconocido', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cli', models.CharField(default='Desconocido', max_length=20)),
                ('apaterno_cli', models.CharField(default='Desconocido', max_length=20)),
                ('amaterno_cli', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('rut_cli', models.CharField(default='00000000', max_length=8)),
                ('dv_cli', models.CharField(default='0', max_length=1)),
                ('mail_cli', models.EmailField(blank=True, default='', max_length=30, null=True)),
                ('pass_cli', models.CharField(default='password', max_length=20)),
                ('numero_cli', models.CharField(blank=True, default='000000000', max_length=9, null=True)),
                ('direccion_cli', models.CharField(blank=True, default='Sin dirección', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_marca', models.CharField(default='Desconocido', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_sucursal', models.CharField(default='Desconocido', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
        migrations.AddField(
            model_name='categoria',
            name='nom_categoria',
            field=models.CharField(default='Desconocido', max_length=30),
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, default='Sin descripción', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='modelo',
            field=models.CharField(blank=True, default='N/A', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='nom_producto',
            field=models.CharField(default='Producto Desconocido', max_length=30),
        ),
        migrations.AddField(
            model_name='producto',
            name='sku',
            field=models.CharField(default='N/A', max_length=12),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ferreApp.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_trab', models.CharField(default='Desconocido', max_length=20)),
                ('apaterno_trab', models.CharField(default='Desconocido', max_length=20)),
                ('amaterno_trab', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('rut_trab', models.CharField(default='00000000', max_length=8)),
                ('dv_trab', models.CharField(default='0', max_length=1)),
                ('mail_trab', models.EmailField(blank=True, default='', max_length=30, null=True)),
                ('pass_trab', models.CharField(default='password', max_length=20)),
                ('cargo', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='ferreApp.cargo')),
                ('sucursal', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='ferreApp.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ferreApp.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ferreApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_boleta', models.DateField()),
                ('cantidad', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ferreApp.cliente')),
                ('producto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ferreApp.producto')),
                ('trabajador', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ferreApp.trabajador')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ferreApp.marca'),
        ),
    ]
