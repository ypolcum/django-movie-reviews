from django.urls import path
from .views import (ReviewListView, 
					MovieDetailView, 
					ReviewCreateView,
					UserReviewListView
					)
from . import views

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews-home'),
    path('user/<str:username>', UserReviewListView.as_view(), name='user-reviews'),
    path('review/new/', ReviewCreateView.as_view(), name='review-create'),
    path('movie_detail/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('byyear/', views.byyear, name='reviews-byyear'),
    path('movies/movies_2020', views.movies_2020, name='reviews-movies-2020'),
    path('movies/movies_2019', views.movies_2019, name='reviews-movies-2019'),
    path('movies/movies_2018', views.movies_2018, name='reviews-movies-2018'),
    path('movies/movies_2017', views.movies_2017, name='reviews-movies-2017'),
    path('movies/movies_2016', views.movies_2016, name='reviews-movies-2016'),
]
