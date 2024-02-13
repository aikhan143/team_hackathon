# Generated by Django 4.2.10 on 2024-02-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('activation_code', models.BooleanField(blank=True, max_length=30)),
                ('is_brand', models.BooleanField(default=False)),
                ('brand', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
