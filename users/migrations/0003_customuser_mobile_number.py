# Generated by Django 4.1.2 on 2024-01-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
