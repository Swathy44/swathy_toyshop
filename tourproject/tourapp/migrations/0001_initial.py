# Generated by Django 4.1.5 on 2023-02-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fru', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('veg', models.CharField(max_length=250)),
                ('dsp', models.TextField()),
            ],
        ),
    ]