# Generated by Django 2.2.16 on 2020-10-31 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riperCars', '0005_auto_20201028_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormInsumo',
            fields=[
                ('nombre', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]