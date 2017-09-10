from django import forms
from django.core.exceptions import ValidationError

# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "邮箱/手机", "required": "required", }),
                               max_length=50, error_messages={"required": "username不能为空", })
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required", }),
                               max_length=50, error_messages={"required": "password不能为空"})

# 邮箱注册表单
class EmailRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "请输入邮箱账号", "required": "required", }),
                             max_length=50, error_messages={"required": "email不能为空", })
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "设置密码", "required": "required", }),
                               max_length=50, error_messages={"required": "password不能为空"})
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "确认密码", "required": "required", }),
                               max_length=50, error_messages={"required": "password不能为空"})

    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     password_repeat = self.cleaned_data.get("password_repeat")
    #     if password and password_repeat and password != password_repeat:
    #         raise forms.ValidationError("两次输入的密码不一致")
    #     return password_repeat

# 手机注册表单
class PhoneRegisterForm(forms.Form):
    phone_num = forms.IntegerField()
    confirm_code = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "设置密码", "required": "required", }),
                               max_length=50, error_messages={"required": "password不能为空"})
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "确认密码", "required": "required", }),
        max_length=50, error_messages={"required": "password不能为空"})

    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     password_repeat = self.cleaned_data.get("password_repeat")
    #     if password and password_repeat and password != password_repeat:
    #         raise forms.ValidationError("两次输入的密码不一致")
    #     return password_repeat