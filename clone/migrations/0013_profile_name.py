# Generated by Django 3.2.5 on 2021-07-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0012_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
