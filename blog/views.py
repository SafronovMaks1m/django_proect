from django.shortcuts import render
  
def index(request):
    return render(request, 'blog/index.html', context = {'body': '<h1>Hello World!</h1>'})

from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'index.html')

from django.shortcuts import render

def profile(request):
    data = request.GET.dict()
    return render(request, 'profile.html', context = data)