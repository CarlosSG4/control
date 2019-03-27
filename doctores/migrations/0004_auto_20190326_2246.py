# Generated by Django 2.1.7 on 2019-03-27 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctores', '0003_auto_20190326_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('image', models.ImageField(default='default.jpg', upload_to='docs_pics')),
                ('genero', models.CharField(blank=True, choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre')], max_length=16)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('numero_celular', models.CharField(max_length=10, null=True, unique=True)),
                ('cedula', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='medico',
        ),
    ]