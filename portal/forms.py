from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import User, Exeat, ExeatExtension


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)


class ExeatForm(ModelForm):
    class Meta:
        model = Exeat
        exclude = ('user', 'status', 'date_created')


class ExtensionForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ExtensionForm, self).__init__(*args, **kwargs)
        self.fields['exeat'].queryset = Exeat.objects.filter(user__username=user, status="A",
                                                             security__clocked_out__isnull=False,
                                                             security__clocked_in__isnull=True)

    class Meta:
        model = ExeatExtension
        exclude = ('approval', 'disapproval_reason')
        widgets = {
            'Reason': forms.Textarea(attrs={'class': 'form-control inputs-2', 'style': "height:150px;"}),
            # 'exeat': forms.ChoiceField(attrs={'class': 'form-control inputs-2'})
        }
