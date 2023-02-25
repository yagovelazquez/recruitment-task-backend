# Generated by Django 4.1.7 on 2023-02-25 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('_id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('guid', models.CharField(max_length=36)),
                ('is_active', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]