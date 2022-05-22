from django import forms
from django.contrib.auth.models import User
from .models import UserInfo


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码：', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码：', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')  # 声明记录的数据

    def clean_password2(self):  # 检查密码是否一致
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('密码不匹配')
        return cd['password2']


class UserRegistrationInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('phone',)


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('birth', 'phone', 'school', 'company', 'profession', 'address', 'about_me')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
