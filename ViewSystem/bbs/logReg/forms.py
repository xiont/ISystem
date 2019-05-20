#encoding:utf-8
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput

"""class LoginForm(forms.Form):
    username = forms.CharField(
            required = True,
            label=u"用户名",
            error_messages={'required':'请输入用户名'},
            widget=forms.TextInput(
                attrs={
                    'placeholder':u"用户名",
                    }
                )
            )

    password = forms.CharField(
            required=True,
            label=u"密码",
            error_messages={'required':u'请输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u"密码",
                    }
                ),
            )"""

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm,self).clean()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='pwdAgain',widget=forms.PasswordInput)
    captcha = forms.CharField()
    def pwd_validate(self,p1,p2):
        return p1==p2

class ChangepwdForm(forms.Form):
    old_pwd = forms.CharField(widget=forms.PasswordInput)
    new_pwd = forms.CharField(widget=forms.PasswordInput)
    new_pwd2 = forms.CharField(label='pwdAgain',widget=forms.PasswordInput)

class User_settingForm(forms.Form):
    photo = forms.CharField(required=False)