# Generated by Django 4.2.6 on 2023-10-11 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='full_name',
            new_name='fullname',
        ),
    ]