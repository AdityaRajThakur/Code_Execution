# Generated by Django 4.2.3 on 2023-08-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Executor', '0006_codingproblem_outputparameter_inputparameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
