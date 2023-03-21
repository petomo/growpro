# Generated by Django 4.1.7 on 2023-03-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grapql', '0013_alter_invoice_status_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_item',
            name='number',
            field=models.FloatField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice_item',
            name='price',
            field=models.FloatField(default=0, max_length=200),
        ),
    ]
