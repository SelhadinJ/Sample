# Generated by Django 4.1.2 on 2023-02-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, unique=True)),
                ('last_name', models.CharField(max_length=256)),
                ('major', models.CharField(max_length=256)),
                ('dob', models.DateField()),
            ],
        ),
    ]