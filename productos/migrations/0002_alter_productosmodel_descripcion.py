# Generated by Django 4.0.4 on 2023-02-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosmodel',
            name='descripcion',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
