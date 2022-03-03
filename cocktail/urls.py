from django.urls import path
from . import views

urlpatterns = [
    path("", views.list, name='list'),
    path("<int:cocktail_id>/", views.recipes),
    path("basesprite/", views.basesprite),
    path("basesprite/<base_name>/", views.listbybase),
]
