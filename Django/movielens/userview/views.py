from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Movie,  Rating, Comments
from django.views import generic
from .forms import NewUserForm, MovieSearchForm, MovieForm
from django.db.models import Avg,F
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required



def index(request : HttpRequest):
    movies = Movie.objects.order_by('-title')
    template = loader.get_template('userview/home.html')
    context = {
    'movies' : movies
    }
    return HttpResponse(template.render(context,request))




def view_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    image_filename = f'{movie_id}.jpg'  # Assuming the image file name is based on the movie ID

    ratings = Rating.objects.filter(movie=movie).values('value').annotate(avg_rating=Avg('value'))
    rating_avg = round(ratings.aggregate(Avg('value'))['value__avg'])

    return render(request, 'userview/movie.html', {
        'movie': movie,
        'image_filename': image_filename,
        'ratings': ratings,
        'rating_avg': rating_avg,
    })
@staff_member_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'userview/admin_creation_page.html', {'form': form})

def search_movies(request):
    genre = request.GET.get('genre', '')
    title = request.GET.get('title', '')
    min_rating = request.GET.get('min_rating', '')

    # Filter movies based on the provided search criteria
    movies = Movie.objects.all()
    if genre:
        movies = movies.filter(genre__icontains=genre)
    if title:
        movies = movies.filter(title__icontains=title)
    if min_rating:
        movies = movies.filter(rating__gte=min_rating)

    paginator = Paginator(movies, 10)  # Display 10 movies per page
    page_number = request.GET.get('page')
    page_movies = paginator.get_page(page_number)

    context = {
        'movies': page_movies,
        'genre': genre,
        'title': title,
        'min_rating': min_rating,
    }

    return render(request, 'userview/search_movies.html', context)

def movies_view(request: HttpRequest):
    movie_list = Movie.objects.order_by('-title')

    # Get the filter values from the request GET parameters
    genre = request.GET.get('genre')
    title = request.GET.get('title')
    min_rating = request.GET.get('min_rating')

    # Apply the filters if provided
    if genre:
        movie_list = movie_list.filter(genre__icontains=genre)
    if title:
        movie_list = movie_list.filter(title__icontains=title)
    if min_rating:
        movie_list = movie_list.filter(rating__gte=float(min_rating))

    paginator = Paginator(movie_list, 10)  # Show n movies per page

    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    template = loader.get_template('userview/movies.html')
    context = {
        'movies': movies,
        'pagination': movies,
    }
    return HttpResponse(template.render(context, request))



def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
            messages.error(request, "Unsuccessful registration. Invalidinformation.")
    return render (request=request, template_name="userview/register.html", context={"register_form":form})


class IndexView(generic.ListView):
    template_name = 'userview/index.html'
    context_object_name = 'movies'
    def get_queryset(self):
        return Movie.objects.order_by('-title')
class MovieView(generic.DetailView):
    model = Movie
    template_name = 'userview/movies.html'

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'userview/login.html')

def logout_request(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('home')

def ratings(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            movie_id = request.POST.get('movie')
            rating_value = request.POST.get('rating')

            try:
                movie = Movie.objects.get(movieid=movie_id)
                rating = Rating.objects.create(value=rating_value, movie=movie, user=request.user)
                rating.save()
            except Movie.DoesNotExist:
                # Handle the case where the movie does not exist
                pass

        movies = Movie.objects.all()
        ratings = Rating.objects.filter(user=request.user)
        return render(request, 'userview/ratings.html', {'movies': movies, 'ratings': ratings})
    else:
        return render(request, 'userview/ratings.html')