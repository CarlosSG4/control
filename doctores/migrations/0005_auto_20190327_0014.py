# Generated by Django 2.1.7 on 2019-03-27 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctores', '0004_auto_20190326_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
