from django.shortcuts import render, redirect
from .models import Idea, Like
from django.http import JsonResponse
from .forms import *

def ideas_list(request):
    if request.method == 'POST':
        sort_option = request.POST.get('sort_option')
        ideas = Idea.objects.all().order_by(sort_option)
        return render(request, 'ideas/ideas_list.html', {'ideas': ideas})
    
    ideas = Idea.objects.all().order_by('id')
    return render(request, 'ideas/ideas_list.html',  {'ideas': ideas})


def ideas_create(request):
    if request.method == 'GET':
        form = IdeaForm()
        ctx = {'form' : form}
        return render(request, 'ideas/idea_create.html', ctx)
    
    form = IdeaForm(request.POST, request.FILES)
    
    if form.is_valid():
        form = form.save()
    return redirect('ideas:detail', form.id)

def idea_detail(request, pk):
    idea = Idea.objects.get(id = pk)
    ctx = {'idea' : idea}
    return render(request, 'ideas/idea_detail.html', ctx)

def idea_delete(request, pk):
    if request.method == 'POST':
        Idea.objects.get(id = pk).delete()
    return redirect('/')

def idea_update(request, pk):
    idea = Idea.objects.get(id = pk)
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        ctx = {'form' : form, "pk" : pk}
        return render(request, 'ideas/idea_update.html', ctx)
    form =IdeaForm(request.POST, request.FILES, instance=idea)
    
    if form.is_valid():      
        form.save()
    return redirect('ideas:detail', pk)
