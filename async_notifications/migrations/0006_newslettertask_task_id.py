# Generated by Django 3.1.1 on 2020-09-08 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('async_notifications', '0005_auto_20200517_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettertask',
            name='task_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
