from django.urls import path
from . import views
from .views import CityDetailView  # Import CityDetailView

urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cities/', views.CityListView, name='cities'),
    path('city/<int:pk>/', CityDetailView.as_view(), name='city-details'),]


"""
.as_view()
city-detail
"""