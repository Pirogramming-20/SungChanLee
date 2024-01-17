from django import forms
from .models import DevTool

class DevToolForm(forms.ModelForm):
    class Meta():
        model = DevTool
        fields = ('__all__')
        labels = {
            'name': '개발툴 이름',
            'kind': '종류',
            'content': '내용'
        }