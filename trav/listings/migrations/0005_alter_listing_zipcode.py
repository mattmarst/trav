# Generated by Django 4.2.7 on 2023-12-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_bath_alter_listing_bed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.IntegerField(default=None),
        ),
    ]