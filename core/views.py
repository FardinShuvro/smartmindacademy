from django.shortcuts import render

def home_en(request):
    return render(request, 'home_en.html')

def home_bn(request):
    return render(request, 'home_bn.html')

# ADD THESE TWO NEW VIEWS:
def subjects_en(request):
    return render(request, 'subjects_en.html')

def resources_en(request):
    return render(request, 'resources_en.html')

def subjects_bn(request):
    return render(request, 'subjects_bn.html')

def resources_bn(request):
    return render(request, 'resources_bn.html')
