# Generated by Django 4.2 on 2023-05-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.CharField(choices=[('HR', 'HR'), ('Engineering', 'Engineering'), ('Marketing', 'Marketing'), ('Planning', 'Planning'), ('Sales', 'Sales'), ('Finance', 'Finance'), ('Operations', 'Operations')], max_length=100),
        ),
    ]
