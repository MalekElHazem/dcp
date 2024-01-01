# Generated by Django 4.2.6 on 2023-11-27 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='events/')),
                ('dateD', models.DateField()),
                ('dateF', models.DateField()),
            ],
        ),
    ]
