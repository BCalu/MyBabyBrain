# Generated by Django 2.0.4 on 2018-06-05 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='usuario_login',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='login.Credenciales'),
        ),
        migrations.AlterField(
            model_name='pariente',
            name='usuario_login',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='login.Credenciales'),
        ),
    ]