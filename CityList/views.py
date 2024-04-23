import random

from django.db.models import F
from django import forms
from django.http import HttpResponseRedirect
from .forms import CityForm, LoginForm, CitySearchForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import DetailView, CreateView
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required


def index(request):
    # Check if there are any cities available
    cities = City.objects.filter(is_active=True)
    if cities.exists():
        # Retrieve a random city
        random_city = random.choice(cities)
    else:
        random_city = None

    context = {
        'random_city': random_city
    }
    return render(request, 'CityList/index.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Authentication successful, redirect to a success page
            return HttpResponseRedirect('/success/')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    return render(request, 'registration/logout.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['CityStaff'])
def edit_city(request, pk):
    city = get_object_or_404(City, pk=pk, user=request.user)  # Filter city by user
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('cities')  # Redirect to the city list page after saving changes
    else:
        form = CityForm(instance=city)  # Populate the form with the city data
    return render(request, 'CityList/edit_city.html', {'city': city, 'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['CityStaff'])
def delete_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    # Check if the request method is POST
    if request.method == 'POST':
        # Delete the city
        city.delete()
        # Redirect to a success URL, like the city list page
        return redirect('cities')
    return render(request, 'CityList/cities.html', {'city': city})


@login_required(login_url='login')
def CityListView(request):
    context = {}
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)  # Create a new city object without saving to database yet
            if request.user.is_authenticated:  # Check if user is authenticated
                city.user = request.user  # Associate the current user with the city
            city.save()  # Save the city object to the database
            # Redirect to the same page to display the form again
            return redirect('cities')
        else:
            print("Form is invalid")
    else:  # If it's a GET request, display the form
        form = CityForm()

    # Get all city objects
    city_objects = City.objects.all()

    context['form'] = form
    context['city_objects'] = city_objects

    if 'view' in request.GET:
        # Assuming 'view' is a button to view details of a specific city
        # Handle the view action here
        return render(request, 'CityList/city-details.html', context)

    elif 'delete' in request.POST:
        # Handle the delete action here
        pk = request.POST.get('delete')
        city = City.objects.get(id=pk)
        city.delete()
        return redirect('cities')

    return render(request, 'CityList/cities.html', context)

"""def CityDetailView(request, pk):
    # Retrieve the city instance or return a 404 error if not found
    city = get_object_or_404(City, id=pk)
    context = {
        'city': city
    }
    # form = CityForm(instance=city)
    return render(request, 'city-details.html', context)
"""


class CityDetailView(DetailView):
    model = City
    template_name = 'CityList/city-details.html'  # Specify the template name


def city_search_view(request):
    # Fetch all cities initially
    cities = City.objects.all()
    print("Cities: ", cities)
    print(1)
    form = CitySearchForm(request.GET)
    print(2)
    if form.is_valid():
        min_walk_score = request.GET.get('min_walk_score')
        print(3)
        print("min walk score:", min_walk_score)
        cities = form.filter_queryset(cities)
        print(4)
        if min_walk_score and min_walk_score.isdigit():  # Check if min_walk_score is not empty and consists of digits
            min_walk_score = int(min_walk_score)  # Convert to integer
            print(5)
            if 0 <= min_walk_score <= 100:
                cities = cities.filter(walk_score__gte=min_walk_score)
                print(6)
        selected_state = form.cleaned_data.get('state')
        print(7)
        if selected_state:
            cities = cities.filter(state=selected_state)
            print(8)
    else:
        # If no filters are provided, fetch all cities
        form = CitySearchForm()  # Reset form
        title = "Cities"
        print("Form values:", form.cleaned_data)

    # Print the count of cities fetched for debugging
    print("Total Cities:", cities.count())

    # Print the filtered cities queryset for debugging
    print("Filtered Cities:", cities)

    # Ensure title is defined even when no filters are applied
    if 'title' not in locals():
        title = "Cities"

    return render(request, 'CityList/city-search.html', {'form': form, 'cities': cities, 'title': title})