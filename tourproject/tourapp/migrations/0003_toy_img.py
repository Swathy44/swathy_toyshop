# Generated by Django 4.1.5 on 2023-02-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0002_toy_delete_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='img',
            field=models.ImageField(default='sdfgnm', upload_to='gallery'),
            preserve_default=False,
        ),
    ]