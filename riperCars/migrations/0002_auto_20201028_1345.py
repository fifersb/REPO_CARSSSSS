# Generated by Django 2.2.16 on 2020-10-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riperCars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderindex',
            name='ident',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]