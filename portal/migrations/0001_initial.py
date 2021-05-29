# Generated by Django 3.2.3 on 2021-05-19 21:13

import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models

import portal.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_security', models.BooleanField(default=False)),
                ('is_exeat_team', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exeat_type',
                 models.CharField(choices=[('HE', 'Home Exeat'), ('BE', 'Bank Exeat'), ('DE', 'Day Exeat')],
                                  max_length=2)),
                ('reason', models.CharField(max_length=254)),
                ('leave_date', models.DateField()),
                ('return_date', models.DateField(blank=True)),
                ('attachment', models.FileField(blank=True, upload_to=portal.models.content_file_name)),
                ('status',
                 models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('AE', 'Awaiting Exeat Approval')],
                                  default='HE', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('exeat',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='portal.exeat')),
                ('exeat_team_acceptance', models.CharField(choices=[('AC', 'Accept'), ('RJ', 'Reject')], max_length=2)),
                ('dsa_approval', models.CharField(choices=[('AC', 'Accept'), ('RJ', 'Reject')], max_length=2)),
                ('disapproval_reason', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('exeat',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='portal.exeat')),
                ('clocked_in', models.DateField(blank=True)),
                ('clocked_out', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('parent_phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Program', models.CharField(max_length=254)),
                ('hall', models.CharField(
                    choices=[('Peter', 'PETER HALL'), ('John', 'JOHN HALL'), ('Paul', 'PAUL HALL'),
                             ('Daniel', 'DANIEL HALL'), ('Joseph', 'JOSEPH HALL'), ('Esther', 'ESTHER HALL'),
                             ('Deborah', 'DEBORAH HALL'), ('Dorcas', 'DORCAS HALL'), ('Lydia', 'LYDIA HALL'),
                             ('Mary', 'MARY HALL')], max_length=10)),
                ('level', models.CharField(
                    choices=[('100', '100 LEVEL'), ('200', '200 LEVEL'), ('300', '300 LEVEL'), ('400', '400 LEVEL'),
                             ('500', '500 LEVEL')], max_length=3)),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExeatExtension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disapproval_reason', models.CharField(blank=True, max_length=254)),
                ('previous_return', models.DateField()),
                ('return_date', models.DateField()),
                ('approval', models.CharField(choices=[('AC', 'Accept'), ('RJ', 'Reject')], max_length=2)),
                ('exeat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.exeat')),
            ],
        ),
    ]