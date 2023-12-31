from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import UploadTrackForm
from django.urls import reverse
from .models import Artist,Track

# Create your views here.
# def catalog(request):
#     context = {}
#     return render(request, "music/catalog.html", context)

class CatalogView(generic.ListView):
    template_name = "music/catalog.html"
    context_object_name = "track_list"

    def get_queryset(self):
        return Track.objects.all().order_by("artist")

# def upload(request):
#     context = {}
#     return render(request, "music/upload.html", context)

def upload(request):
    if request.method == "POST":
        form = UploadTrackForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect(reverse("music:catalog"))
    else:
        form = UploadTrackForm()
    context = {"form":form}
    return render(request, "music/upload.html", context)