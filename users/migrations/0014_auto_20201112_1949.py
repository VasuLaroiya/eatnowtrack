# Generated by Django 3.0.8 on 2020-11-13 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20201112_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activity_level',
            field=models.CharField(choices=[('Sedentary', 'sedentary'), ('Moderately Active', 'moderately active'), ('Very Active', 'very active')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_goals',
            field=models.CharField(choices=[('Lose Weight', 'lose weight'), ('Maintain Weight', 'maintain weight'), ('Gain Weight', 'gain weight')], default=0, max_length=20),
        ),
    ]