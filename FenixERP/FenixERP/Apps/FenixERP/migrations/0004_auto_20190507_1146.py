# Generated by Django 2.1.7 on 2019-05-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ubicaciones', '0003_auto_20190507_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productotienda',
            name='RefaccionDe',
        ),
        migrations.AddField(
            model_name='productotienda',
            name='RefaccionDe',
            field=models.ManyToManyField(to='Ubicaciones.Auto'),
        ),
    ]
