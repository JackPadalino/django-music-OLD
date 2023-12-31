from django.shortcuts import render
from django.views import generic
from music.models import Artist,Track

# Create your views here.
# def home(request):
#     context = {}
#     return render(request, "main/home.html", context)

class Home(generic.ListView):
    template_name = "main/home.html"
    context_object_name = "track_list"

    def get_queryset(self):
        return Track.objects.all().order_by("-upload_date")