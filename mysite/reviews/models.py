from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Movie(models.Model):
	movie_title = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	release_year = models.DateTimeField()
	genre = models.CharField(max_length=100)
	movie_poster = models.ImageField(upload_to='posters')
	summary = models.TextField()
	cast = models.TextField()

	def __str__(self):
		return self.movie_title

class Review(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{0} Review'.format(self.movie)


	def get_absolute_url(self):
		return reverse('reviews-home')