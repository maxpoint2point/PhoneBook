# Generated by Django 3.1.2 on 2020-10-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='manager',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Менеджер'),
        ),
    ]