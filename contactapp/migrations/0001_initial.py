# Generated by Django 3.2.18 on 2023-03-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=25)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=25)),
            ],
        ),
    ]
