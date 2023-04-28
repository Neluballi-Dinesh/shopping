# Generated by Django 4.1.4 on 2022-12-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('course', models.CharField(max_length=100)),
                ('fee', models.IntegerField()),
                ('iname', models.IntegerField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
