from django.urls import path, include
from . import views
from .views import CityDetailView  # Import CityDetailView

urlpatterns = [
    # URLs built for this app specifically
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cities/', views.CityListView, name='cities'),
    path('edit/<int:pk>/', views.edit_city, name='edit-city'),
    path('delete/<int:pk>/', views.delete_city, name='delete-city'),
    path('city/<int:pk>/', CityDetailView.as_view(), name='city-details'),
    path('city-search/', views.city_search_view, name='city-search'),
]


# additional built-in URLs
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]