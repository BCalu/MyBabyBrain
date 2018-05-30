# Generated by Django 2.0.4 on 2018-05-29 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(help_text='Ejemplo: 12345678-9', max_length=15)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.PositiveIntegerField()),
                ('nacionalidad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=70)),
                ('ciudad', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('estado_civil', models.CharField(choices=[('SO', 'Soltero/a'), ('C', 'Casado/a'), ('V', 'Viudo/a'), ('D', 'Divorciado/a'), ('SE', 'Separado/a')], max_length=2)),
                ('ocupacion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test2.Persona')),
                ('logo', models.ImageField(upload_to='ImagenesMedicos/')),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('telefono_celular', models.CharField(blank=True, max_length=13, null=True)),
                ('telefono_domiclio', models.CharField(blank=True, max_length=13, null=True)),
            ],
            bases=('test2.persona',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test2.Persona')),
                ('alergias', models.TextField(max_length=300)),
                ('enfermedades', models.TextField(max_length=300)),
                ('peraciones', models.TextField(max_length=300)),
                ('farmacos', models.TextField(max_length=300)),
                ('hospitalizaciones', models.TextField(max_length=300)),
                ('medico_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Medico')),
            ],
            bases=('test2.persona',),
        ),
        migrations.CreateModel(
            name='Pariente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test2.Persona')),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('telefono_celular', models.CharField(blank=True, max_length=13, null=True)),
                ('telefono_domiclio', models.CharField(blank=True, max_length=13, null=True)),
            ],
            bases=('test2.persona',),
        ),
        migrations.AddField(
            model_name='paciente',
            name='parientes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Pariente'),
        ),
    ]
