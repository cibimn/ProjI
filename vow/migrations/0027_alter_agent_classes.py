# Generated by Django 4.1.3 on 2022-12-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vow', '0026_remove_customers_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='classes',
            field=models.ManyToManyField(blank=True, to='vow.classes'),
        ),
    ]
