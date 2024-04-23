from django import forms
from django.forms import ModelForm
from .models import City
from django.contrib.auth.forms import AuthenticationForm


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'website', 'is_active', 'state', ]
        # Explicitly mark required fields
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'website': forms.URLInput(attrs={'required': True}),
            'is_active': forms.CheckboxInput(attrs={'required': True}),
            'state': forms.Select(attrs={'required': True}),
        }


class LoginForm(AuthenticationForm):
    pass


class CitySearchForm(forms.Form):
    name = forms.CharField(label='City Name', required=False)
    state_choices = [('', '-- Any State --')] + list(City.States)  # Add the option for Any state
    state = forms.ChoiceField(label='State', choices=state_choices, required=False)
    is_active = forms.BooleanField(label='Active', required=False)
    min_walk_score = forms.IntegerField(label='Minimum Walk Score', required=False)

    def filter_queryset(self, queryset):
        if self.is_valid():
            name = self.cleaned_data.get('name')
            state = self.cleaned_data.get('state')
            is_active = self.cleaned_data.get('is_active')
            min_walk_score = self.cleaned_data.get('min_walk_score')

            if name:
                queryset = queryset.filter(name__icontains=name)
            if state:
                if state != '':  # Check if the state is not empty (i.e., not "Any state")
                    queryset = queryset.filter(state=state)
            if is_active is not None:
                queryset = queryset.filter(is_active=is_active)
            if min_walk_score is not None:
                queryset = queryset.filter(walk_score__gte=min_walk_score)

        return queryset
