# Generated by Django 5.0.2 on 2024-10-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0004_bank_statment_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_username', models.CharField(max_length=100)),
                ('admin_pssword', models.CharField(max_length=100)),
            ],
        ),
    ]
