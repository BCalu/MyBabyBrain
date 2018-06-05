# Generated by Django 2.0.4 on 2018-06-05 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0003_auto_20180605_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pariente',
            name='usuario_login',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Credenciales'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(help_text='Formato: AAAA-MM-DD'),
        ),
    ]