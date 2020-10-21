# Generated by Django 3.1.2 on 2020-10-21 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webui', '0002_phones_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='logging',
            name='phone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='logging_phones', to='webui.phones'),
        ),
        migrations.AlterField(
            model_name='logging',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
    ]
