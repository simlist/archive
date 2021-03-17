from django.urls import path

from . import views

urlpatterns = [
    path(
        '<slug:slug>/',
        views.RecordingDetail.as_view(),
        name='recording_detail'),
    path('', views.RecordingsList.as_view(), name='recordings_list'),
]