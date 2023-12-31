from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from .forms import UploadTrackForm
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

def download(request, pk):
    track = Track.objects.get(pk=pk)
    response = HttpResponse(track.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{track.artist.name} - {track.title}.mp3"'
    return response