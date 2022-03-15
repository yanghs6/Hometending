from django.urls import path
from . import views


app_name = 'cocktail'

urlpatterns = [
    path("", views.list, name='list'),
    path("<int:cocktail_id>/", views.cocktails),
    path("basesprite/", views.basesprite, name='basesprite'),
    path("basesprite/<base_name>/", views.listbybase),
]
