from django.urls import path
from . import views

app_name = "tours"

urlpatterns = [
    path("", views.home, name="home"),
    path("regions/", views.regions, name="regions"),
    path("regions/<slug:slug>/", views.region_detail, name="region_detail"),
    path("tours/", views.tour_list, name="tour_list"),
    path("tours/<slug:slug>/", views.tour_detail, name="tour_detail"),
    path("tours/<slug:slug>/book/", views.book_tour, name="book_tour"),
    path("booking/success/", views.booking_success, name="booking_success"),
]
