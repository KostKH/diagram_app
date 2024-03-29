# Generated by Django 4.2.4 on 2023-08-16 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Название города')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='PlanFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('plan', models.PositiveSmallIntegerField(default=0, verbose_name='План')),
                ('fact', models.PositiveSmallIntegerField(default=0, verbose_name='Факт')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='cities.city', verbose_name='Город: план')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddConstraint(
            model_name='planfact',
            constraint=models.UniqueConstraint(fields=('city', 'year'), name='unique_city_year'),
        ),
    ]
