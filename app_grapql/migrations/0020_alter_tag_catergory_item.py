# Generated by Django 4.1.7 on 2023-03-23 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_grapql', '0019_alter_invoice_item_number_alter_invoice_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_catergory',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_grapql.item'),
        ),
    ]
