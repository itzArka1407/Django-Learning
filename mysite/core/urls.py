from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("recents/", views.note_recent, name="note_recent"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
]
