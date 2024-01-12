from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def review_list(request):
    if request.method == 'POST':
        sort_option = request.POST.get('sort_option')
        reviews = Review.objects.all().order_by( '-' + sort_option)
        return render(request, 'reviews/review_list.html', {'reviews': reviews})
    
    # 기본 --> 별점 순
    reviews = Review.objects.all().order_by('rating')
    return render(request, 'reviews/review_list.html',  {'reviews': reviews})

def review_detail(request, pk):
    review =  Review.objects.get(id = pk)
    running_time = int(review.running_time)
    running_time_hour = running_time // 60
    running_time_min = running_time % 60
    
    context = {
        "review" : review,
        "review_running_time_hour" : running_time_hour,
        "review_running_time_min" : running_time_min,
    }

    return render(request, 'reviews/review_detail.html', context)


def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save_review()
            return redirect('/')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_edit.html', {'form': form})


def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save_review()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_edit.html', {'form': form})


def review_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id = pk)
        review.delete()
    return redirect("/")
