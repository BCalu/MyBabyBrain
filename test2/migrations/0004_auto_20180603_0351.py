# Generated by Django 2.0.4 on 2018-06-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0003_auto_20180603_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pariente',
            name='estado_civil',
            field=models.CharField(choices=[('SO', 'Soltero/a'), ('C', 'Casado/a'), ('V', 'Viudo/a'), ('D', 'Divorciado/a'), ('SE', 'Separado/a')], max_length=2),
        ),
    ]
