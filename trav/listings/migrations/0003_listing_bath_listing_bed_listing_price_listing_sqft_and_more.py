# Generated by Django 4.2.7 on 2023-12-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bath',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='bed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
