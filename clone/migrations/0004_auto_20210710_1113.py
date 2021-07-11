# Generated by Django 3.2.5 on 2021-07-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0003_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
