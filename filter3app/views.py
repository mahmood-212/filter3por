from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict={'text':'hello world','number':1000}
    return render(request,'mood1/index.html',context_dict)

def other(request):
    return render(request,'mood1/othre.html')

def relative_url(request):
    return render(request,'mood1/relative.html')