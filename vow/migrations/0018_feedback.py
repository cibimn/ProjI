# Generated by Django 4.1.3 on 2022-12-02 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vow', '0017_alter_customers_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(choices=[('Good', 'Good'), ('Need Imporovement', 'Need Imporovement'), ('Irrelevant', 'Irrelevant')], max_length=50)),
                ('affirmation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vow.vow')),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
