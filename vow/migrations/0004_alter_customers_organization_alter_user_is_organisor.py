# Generated by Django 4.1.3 on 2022-11-25 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vow', '0003_user_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vow.organization'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=False),
        ),
    ]
