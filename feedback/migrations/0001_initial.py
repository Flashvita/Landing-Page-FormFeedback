# Generated by Django 4.0.4 on 2022-05-07 16:59

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
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
