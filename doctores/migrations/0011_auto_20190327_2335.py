# Generated by Django 2.1.7 on 2019-03-28 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctores', '0010_auto_20190327_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('apaterno', models.TextField(max_length=20)),
                ('amaterno', models.TextField(max_length=20)),
                ('image', models.ImageField(default='default.jpg', upload_to='doctores_pics')),
                ('genero', models.CharField(blank=True, choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre')], max_length=16)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('numero_celular', models.CharField(max_length=10, null=True, unique=True)),
                ('cedula', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctores',
            name='author',
        ),
        migrations.DeleteModel(
            name='Doctores',
        ),
    ]