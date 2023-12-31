# Generated by Django 4.2.5 on 2023-09-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acharyaa', '0002_enrollment_membershipplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='DueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='Price',
            field=models.IntegerField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='paymentStatus',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phonenumber',
            field=models.IntegerField(max_length=12),
        ),
    ]
