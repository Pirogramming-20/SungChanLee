from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta():
        model = Idea
        fields = ('__all__')
        labels = {
            'title': '아이디어 제목',
            'image': '사진',
            'content': '내용',
            'interest' : '관심도'
        }