# Generated by Django 4.1.3 on 2022-11-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vow', '0013_alter_api_key_options_alter_api_key_api_key_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
