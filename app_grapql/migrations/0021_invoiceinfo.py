# Generated by Django 4.1.7 on 2023-03-23 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_grapql', '0020_alter_tag_catergory_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('cause', models.CharField(blank=True, max_length=200, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_grapql.invoice')),
            ],
        ),
    ]