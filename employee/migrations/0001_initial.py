# Generated by Django 4.1.5 on 2023-01-06 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now_add=True)),
                ('employee', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceActions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=100)),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.attendance')),
            ],
        ),
    ]
