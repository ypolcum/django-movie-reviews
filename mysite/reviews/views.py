from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Review, Movie


def home(request):
	context = {
		'reviews': Review.objects.all()
	}
	return render(request, 'reviews/home.html', context)


class ReviewListView(ListView):
	model = Review
	template_name = 'reviews/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'reviews'
	ordering = ['-date_posted']
	paginate_by = 5

class UserReviewListView(ListView):
	model = Review
	template_name = 'reviews/user_reviews.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'reviews'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Review.objects.filter(author=user).order_by('-date_posted')


class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review
	template_name = 'reviews/review_form.html'
	fields = ['movie', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


def about(request):
	return render(request, 'reviews/about.html', {'title': 'About'})

def byyear(request):
	return render(request, 'reviews/byyear.html', {'title': 'Movies by Year'})

def movie_detail(request):
	movies = Movie.objects.all()
	context = {'movies': movies}
	return render(request, 'reviews/movie_detail.html', context)

class MovieDetailView(DetailView):
	model = Movie


#def profile(request):
#	return render(request, 'reviews/profile.html', {'title': 'Profile'})

def movies_2020(request):
	return render(request, 'reviews/movies_2020.html', {'title':'2020'})

def movies_2019(request):
	return render(request, 'reviews/movies_2019.html', {'title':'2019'})

def movies_2018(request):
	return render(request, 'reviews/movies_2018.html', {'title':'2018'})

def movies_2017(request):
	return render(request, 'reviews/movies_2017.html', {'title':'2017'})

def movies_2016(request):
	return render(request, 'reviews/movies_2016.html', {'title':'2016'})
