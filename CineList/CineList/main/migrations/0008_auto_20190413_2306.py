# Generated by Django 2.1.7 on 2019-04-14 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190411_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrequest',
            name='status',
            field=models.CharField(choices=[('S', 'Sent'), ('A', 'Accepted'), ('D', 'Denied'), ('C', 'Cancelled')], default='S', max_length=2),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(choices=[('S', 'Sent'), ('A', 'Accepted'), ('C', 'Cancelled')], default='S', max_length=2),
        ),
    ]