from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.conf import settings
# Create your models here.

# 리뷰 = {
#     영화 제목, 감독, 주연, 장르, 별점, 러닝타임, 리뷰 내용
# }

# models.py

# 리뷰
class Review(models.Model):
    title = models.CharField(max_length=100)
    # 감독
    directors = models.CharField(max_length=100)
    # 배우
    actors = models.CharField(max_length=100)
    # 개봉연도 
    current_year = timezone.now().year
    release_year = models.IntegerField(
        validators=[
            MinValueValidator(1000),  # 최소 연도
            MaxValueValidator(current_year),  # 최대 == 현재 연도
        ]
    )

    # 장르
    GENRE_CHOICES = [
        ('액션', 'Action'),
        ('코미디', 'Comedy'),
        ('드라마', 'Drama'),
        ('로맨스', 'Romance'),
        ('스릴러', 'Thriller'),        
    ]
    genres = models.CharField(max_length=20, choices=GENRE_CHOICES)
    
    # 평점
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, 
        validators=[
            MinValueValidator(0.0), 
            MaxValueValidator(5.0)]
    )

    # 러닝 타임 (분 단위)
    running_time = models.IntegerField()
    
    # 리뷰 내용
    content = models.TextField()
    
    # 여기부턴 사이트에서 보이지 않게
    # 리뷰 쓴 사람
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    # 리뷰 작성 및 수정 시간
    save_date = models.DateTimeField(
            blank=True, null=True)
    # 이미지
    image_url = models.TextField(null=True, blank=True)
    
    # 리뷰를 저장하고 저장한 시간을 기록하는 함수 --> save대신 사용
    def save_review(self):
        self.save_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title