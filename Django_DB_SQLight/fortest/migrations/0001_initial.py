# Generated by Django 3.2.9 on 2022-03-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cryptoPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrumentId', models.CharField(max_length=200)),
                ('depth', models.CharField(max_length=200)),
                ('timestamp', models.CharField(max_length=200)),
            ],
        ),
    ]
