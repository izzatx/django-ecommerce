# Generated by Django 4.1.7 on 2023-05-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_zip_order_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
