import random
from django.views.generic import DetailView
from .forms import CityForm
from django.shortcuts import render
from .models import City


def index(request):
    # Retrieve a random city
    random_city = random.choice(City.objects.filter(is_active=True))

    context = {
        'random_city': random_city
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')





def CityListView(request):
    context = {}
    form = CityForm()
    city_objects = City.objects.all()
    context['city'] = city_objects
    if request.method == 'POST':
        if 'save' in request.POST:
            print("Form is valid")
            form = CityForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print("Form is invalid")
        elif 'view' in request.POST:
            # Assuming 'view' is a button to view details of a specific city
            # Handle the view action here
            return render(request, 'city-details.html', context)
        elif 'delete' in request.POST:
            # Handle the delete action here
            pk = request.POST.get('delete')
            city = City.objects.get(id=pk)
            city.delete()

    elif request.method == 'GET':
        if 'view' in request.GET:
            # Assuming 'view' is a button to view details of a specific city
            # Handle the view action here
            return render(request, 'city-details.html', context)
        context['form'] = form

    return render(request, 'cities.html', context)


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
    template_name = 'city-details.html'  # Specify the template name
