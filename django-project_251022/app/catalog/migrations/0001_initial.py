# Generated by Django 4.1.2 on 2022-10-26 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_ID', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAddress',
            fields=[
                ('address_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.student')),
            ],
        ),
    ]