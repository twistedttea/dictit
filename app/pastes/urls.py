from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_paste, name="create_paste"),
    path("p/<str:short_id>/", views.view_paste, name="view_paste"),
    path("s/", views.search_paste, name="search_paste"),
]
