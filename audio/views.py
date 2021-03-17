from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class RecordingsList(ListView):
    model = models.Recording
    template_name = 'audio/recordings_list.html'
    context_object_name = 'recordings'


class RecordingDetail(DetailView):
    model = models.Recording
    template_name = 'audio/recording_detail.html'
    context_object_name = 'recording'


def recordings_list(request):
    recordings = models.Recording.objects.all()
    return render(request, 'audio/list.html', {'recordings': recordings})