# Generated by Django 3.0.8 on 2020-11-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20201112_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
