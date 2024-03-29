# Generated by Django 2.1.7 on 2019-05-01 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MarcaAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(default='Sin descripcion', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MarcaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(default='Sin descripcion', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoTienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.CharField(max_length=6)),
                ('Descripcion', models.CharField(default='Sin descripcion', max_length=50)),
                ('imagen', models.ImageField(upload_to='')),
                ('Activo', models.BooleanField(default=True)),
                ('MarcaProd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubicaciones.MarcaProducto')),
                ('RefaccionDe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubicaciones.Auto')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Calle', models.CharField(max_length=50)),
                ('Numero', models.CharField(max_length=4)),
                ('Colonia', models.CharField(max_length=50)),
                ('Municipio', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=50)),
                ('codigoPostal', models.CharField(max_length=6)),
                ('urlDireccion', models.CharField(max_length=300)),
                ('FechaRegistro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='productotienda',
            name='Tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubicaciones.Tienda'),
        ),
        migrations.AddField(
            model_name='auto',
            name='MarcAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubicaciones.MarcaAuto'),
        ),
    ]
