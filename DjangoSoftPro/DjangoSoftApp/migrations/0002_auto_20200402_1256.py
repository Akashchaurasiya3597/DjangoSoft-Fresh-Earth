# Generated by Django 3.0 on 2020-04-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoSoftApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitsdatabase',
            name='Big_image',
            field=models.ImageField(blank=True, upload_to='Fruits/'),
        ),
        migrations.AlterField(
            model_name='fruitsdatabase',
            name='First_image',
            field=models.ImageField(blank=True, upload_to='Fruits/'),
        ),
        migrations.AlterField(
            model_name='fruitsdatabase',
            name='Second_image',
            field=models.ImageField(blank=True, upload_to='Fruits/'),
        ),
    ]