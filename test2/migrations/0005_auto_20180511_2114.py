# Generated by Django 2.0.3 on 2018-05-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0004_auto_20180511_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.EmailField(max_length=120),
        ),
    ]
