# Generated by Django 3.2.3 on 2021-05-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('portal', '0006_alter_exeat_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='clocked_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='clocked_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
