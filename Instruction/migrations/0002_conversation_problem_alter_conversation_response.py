# Generated by Django 4.2.7 on 2023-12-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instruction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='problem',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='response',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
