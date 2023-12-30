from django.shortcuts import render

# Create your views here.
def catalog(request):
    context = {}
    return render(request, "music/catalog.html", context)

def upload(request):
    context = {}
    return render(request, "music/upload.html", context)