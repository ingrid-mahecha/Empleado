# Generated by Django 4.2.6 on 2023-10-10 02:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, verbose_name='skill')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('lastname', models.CharField(max_length=50, verbose_name='lastName')),
                ('job', models.CharField(choices=[('0', 'Ingeniero'), ('1', 'Arquitecto'), ('2', 'Desarrollador'), ('3', 'Programador')], max_length=1, verbose_name='job')),
                ('cv', ckeditor.fields.RichTextField(blank=True, default='None')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='fullName')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('skills', models.ManyToManyField(to='employer.skills')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]