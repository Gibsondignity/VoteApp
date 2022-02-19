from . import views
from django.urls import include, path

urlpatterns = [
    path('movie_title/', views.MovieTitleApi, name="movie_title"),
    path('nominees/', views.NominationApi, name="nominees"),
    path('categories/', views.CategoryApi, name="categories"),
]