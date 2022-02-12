from django.urls import path

from frontend.views import index

urlpatterns = [
    path("", index, name="index"),
]
