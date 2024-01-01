# Generated by Django 4.2.6 on 2023-11-28 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_club', '0002_event'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='event',
            table='event',
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_club.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_club.member')),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
    ]
