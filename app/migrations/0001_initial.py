# Generated by Django 5.0.6 on 2024-07-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('passw', models.CharField(max_length=20)),
                ('rpass', models.CharField(max_length=20)),
            ],
        ),
    ]
