import os

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_security = models.BooleanField(default=False)
    is_exeat_team = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    Hall_Choices = [
        ('Peter', 'PETER HALL'),
        ('John', 'JOHN HALL'),
        ('Paul', 'PAUL HALL'),
        ('Daniel', 'DANIEL HALL'),
        ('Joseph', 'JOSEPH HALL'),
        ('Esther', 'ESTHER HALL'),
        ('Deborah', 'DEBORAH HALL'),
        ('Dorcas', 'DORCAS HALL'),
        ('Lydia', 'LYDIA HALL'),
        ('Mary', 'MARY HALL'),
    ]
    Level_Choices = [
        ('100', '100 LEVEL'),
        ('200', '200 LEVEL'),
        ('300', '300 LEVEL'),
        ('400', '400 LEVEL'),
        ('500', '500 LEVEL'),
    ]
    Gender = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    parent_phone_no = PhoneNumberField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=Gender)
    Program = models.CharField(max_length=254)
    hall = models.CharField(max_length=10, choices=Hall_Choices)
    level = models.CharField(max_length=3, choices=Level_Choices)

    def __str__(self):
        return f'{self.user.username} Profile'

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def create_exeat_approval(sender, instance, created, **kwargs):
    if created:
        Approval.objects.create(exeat=instance)


def create_exeat_security(sender, instance, created, **kwargs):
    if created:
        Security.objects.create(exeat=instance)


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.id, ext)
    return os.path.join('uploads/%Y/%m', filename)


class Exeat(models.Model):
    Status_Choices = [
        ('P', 'Pending'),
        ('D', 'Disproved'),
        ('AD', 'Awaiting Dean Approval'),
        ('AE', 'Awaiting Acceptance'),
        ('A', 'Approved')
    ]
    Exeat_Choices = [
        ('HE', 'Home Exeat'),
        ('BE', 'Bank Exeat'),
        ('DE', 'Day Exeat'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exeat_type = models.CharField(max_length=2, choices=Exeat_Choices)
    reason = models.CharField(max_length=254)
    leave_date = models.DateField()
    return_date = models.DateField(blank=True)
    attachment = models.FileField(upload_to='uploads/%Y%m%d', blank=True)
    status = models.CharField(choices=Status_Choices, max_length=2, default=Status_Choices[0][0])
    date_created = models.DateTimeField(default=timezone.now)


class Approval(models.Model):
    Approval_Choices = [
        ('PE', 'Pending'),
        ('AC', 'Accept'),
        ('RJ', 'Reject'),
    ]
    exeat = models.OneToOneField(Exeat, on_delete=models.CASCADE, primary_key=True)
    exeat_team_acceptance = models.CharField(max_length=2, choices=Approval_Choices, default=Approval_Choices[0][0])
    dsa_approval = models.CharField(max_length=2, choices=Approval_Choices, default=Approval_Choices[0][0])
    disapproval_reason = models.CharField(max_length=254, blank=True)


class Security(models.Model):
    exeat = models.OneToOneField(Exeat, on_delete=models.CASCADE, primary_key=True)
    clocked_in = models.DateTimeField(blank=True, null=True)
    clocked_out = models.DateTimeField(blank=True, null=True)


class ExeatExtension(models.Model):
    Approval_Choices = [
        ('AC', 'Accept'),
        ('RJ', 'Reject'),
    ]
    exeat = models.ForeignKey(Exeat, on_delete=models.CASCADE)
    disapproval_reason = models.CharField(max_length=254, blank=True)
    return_date = models.DateField()
    approval = models.CharField(choices=Approval_Choices, max_length=2)


post_save.connect(create_user_profile, sender=User)
post_save.connect(create_exeat_approval, sender=Exeat)
post_save.connect(create_exeat_security, sender=Exeat)
