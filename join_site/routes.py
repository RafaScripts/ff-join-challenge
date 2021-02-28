from django.urls import include, path

from join_site import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
