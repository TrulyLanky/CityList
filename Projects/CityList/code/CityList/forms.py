from django.forms import ModelForm
from .models import Project, Portfolio, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# create class for project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', ]


# create class for project form
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'contact_email', 'is_active', 'about', ]


# create class for project form
class CreateUserForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', ]


# create class for project form
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'major', 'portfolio', ]
