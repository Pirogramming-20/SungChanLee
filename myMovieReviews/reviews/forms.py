from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'directors', 'release_year', 'actors', 'genres', 'rating', 'running_time', 'content', 'image_url')
        labels = {
            'title' : '영화 제목', 
            'directors' : '감독', 
            'release_year' : '개봉연도', 
            'actors' : '주연 배우', 
            'genres' : '장르', 
            'rating' : '평점', 
            'running_time' : '러닝 타임', 
            'content' : '리뷰',
            'image_url' : '이미지 url(없을 경우 공백)'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].required = False