from django.conf.urls import url
from pelicula import views

urlpatterns = [
    url(r'^api/pelicula$', views.pelicula_list),
    url(r'^api/pelicula/(?P<pk>[0-9]+)', views.pelicula_detail),
    url(r'^api/pelicula/published$', views.pelicula_list_published)
]