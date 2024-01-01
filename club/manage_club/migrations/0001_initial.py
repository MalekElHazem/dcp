# Generated by Django 4.2.6 on 2023-11-26 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mFname', models.CharField(max_length=200)),
                ('mLname', models.CharField(max_length=200)),
                ('memail', models.EmailField(max_length=200)),
                ('mphone', models.CharField(max_length=200)),
                ('mdep', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]