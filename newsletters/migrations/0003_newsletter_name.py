# Generated by Django 4.1.4 on 2022-12-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_alter_client_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]