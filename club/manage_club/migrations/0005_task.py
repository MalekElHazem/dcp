# Generated by Django 4.2.6 on 2023-11-29 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_club', '0004_remove_attendance_attendance_date_attendance_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_club.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_club.member')),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
