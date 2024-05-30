# Generated by Django 3.2 on 2024-01-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210513_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='sea_rch',
            name='Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='con_tact',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='con_tact',
            name='subject',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='donor_registration',
            name='home_address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='donor_registration',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]