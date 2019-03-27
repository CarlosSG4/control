# Generated by Django 2.1.7 on 2019-03-27 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_consultorio_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('genero', models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=16)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('numero_celular', models.CharField(max_length=10, null=True, unique=True)),
                ('curp', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('direccion', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
