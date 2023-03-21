# Generated by Django 4.1.7 on 2023-03-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grapql', '0002_chat_id_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='id_chat',
        ),
        migrations.AddField(
            model_name='supplier',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='stastus',
            field=models.CharField(choices=[(1, 'Addition'), (2, 'Change'), (3, 'Deletion'), (4, 'Cancel'), (5, 'Send'), (6, 'Read')], default='create', max_length=50),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status_now',
            field=models.CharField(choices=[(1, 'Addition'), (3, 'Deletion'), (4, 'Cancel'), (7, 'Complete')], default='create', max_length=50),
        ),
        migrations.AlterField(
            model_name='invoice_history',
            name='status',
            field=models.CharField(choices=[(1, 'Addition'), (3, 'Deletion'), (4, 'Cancel'), (7, 'Complete')], default='create', max_length=50),
        ),
    ]
