# Generated by Django 3.2.3 on 2021-05-20 00:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exeat',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('AE', 'Awaiting Exeat Approval')],
                                   default='P', max_length=2),
        ),
    ]
