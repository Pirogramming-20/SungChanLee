from django.shortcuts import render, redirect
from .models import DevTool
from .forms import *

def devtools_list(request):
    devtools = DevTool.objects.all() 
    return render(request, 'devtools/devtools_list.html', {'devtools' : devtools })

def devtool_create(request):
    if request.method == 'GET':
        form = DevToolForm()
        ctx = {'form' : form}
        return render(request, 'devtools/devtool_create.html', ctx)
    form = DevToolForm(request.POST, request.FILES)
    if form.is_valid():
        form = form.save()
    return redirect('devtools:detail', form.id)


def devtool_detail(request, pk):
    devtool = DevTool.objects.get(id = pk)
    related_ideas = devtool.idea_set.all()
    ctx = {'devtool' : devtool , 'related_ideas' : related_ideas}
    return render(request, 'devtools/devtool_detail.html', ctx)

 
def devtool_update(request, pk):
    devtool = DevTool.objects.get(id = pk)
    if request.method == 'GET':
        form = DevToolForm(instance=devtool)
        ctx = {'form' : form, "pk" : pk}
        return render(request, 'devtools/devtool_update.html', ctx)
    form = DevToolForm(request.POST, request.FILES, instance=devtool)
    
    if form.is_valid():      
        form.save()
    return redirect('devtools:detail', pk)

def devtool_delete(request, pk):
    if request.method == 'POST':
        DevTool.objects.get(id = pk).delete()
    return redirect('devtools:list')
