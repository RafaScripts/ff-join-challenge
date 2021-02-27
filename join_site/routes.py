from django.urls import include, path

from join_site import views


urlpatterns = [
    path('', views.index),
]
