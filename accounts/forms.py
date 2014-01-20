from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.models import ModelForm
from accounts.models import UserProfile
from utils.forms import MyDateInput
from django.forms.widgets import Textarea




class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget=forms.TextInput(attrs={'required': 'required', 'autocomplete': 'off'}),
                                label=_("Username"),
                                error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': 'required', 'max_length': '70', 'autocomplete': 'off'}),
                             label=_("Email address"))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'required', 'autocomplete': 'off'}, render_value=False), 
                                label=_("Password"))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'required', 'autocomplete': 'off'}, render_value=False),
                                label=_("Password (again)"))
                                
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required': 'required', 'style': 'display:inline;'}),
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={ 'required': _("You must agree to the terms to register") })

    
    def clean_username(self):
        """
        Validate that the username is not already in use.
        
        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("A user with that username already exists."))

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data



class EditUserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)        
        self.fields['age'].widget = MyDateInput()
        self.fields['about'].widget = Textarea()
        
    class Meta:
        model = UserProfile
        fields = ['native_lang', 'learning_lang', 'about', 'city', 'age']
        

class EditUserForm(ModelForm):
    
    class Meta:  
        model = User
        fields = ['first_name', 'last_name', 'email',]



