# Generated by Django 2.2.16 on 2020-10-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riperCars', '0002_auto_20201028_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosGaleria',
            fields=[
                ('ident', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='cars')),
            ],
        ),
    ]
