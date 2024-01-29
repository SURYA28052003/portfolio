# myapp/forms.py
from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'email', 'phone', 'message']
        
    # def __init__(self, *args, **kwargs):
    #     super(UserInfoForm, self).__init__(*args, **kwargs)

    # for field_name in self.fields:
    #         self.fields[field_name].widget.attrs['autocomplete'] = field_name