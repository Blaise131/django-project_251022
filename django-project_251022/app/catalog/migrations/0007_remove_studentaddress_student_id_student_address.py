# Generated by Django 4.1.2 on 2022-10-26 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_student_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentaddress',
            name='Student_ID',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.studentaddress'),
        ),
    ]
