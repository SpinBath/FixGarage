from django import forms
from django.db import models
from .models import Clients, Vehicles, Services, Billing


class clientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'address', 'phone', 'email']

class vehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicles
        fields = ['owner', 'brand', 'model', 'year', 'license_plate']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Sacamos el usuario de los argumentos
        super(vehicleForm, self).__init__(*args, **kwargs)

        self.fields['owner'].queryset = Clients.objects.filter(user=user)
    
class servicesForm(forms.ModelForm):
     
    class Meta:
        model = Services
        fields = ['vehicle', 'owner','description','departure_date','entry_date', 'price']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Sacamos el usuario de los argumentos
        super(servicesForm, self).__init__(*args, **kwargs)

        self.fields['vehicle'].queryset = Vehicles.objects.filter(user=user)
        self.fields['owner'].queryset = Clients.objects.filter(user=user)

class billingForm(forms.ModelForm):

    class Meta:
        model = Billing
        fields = ['vehicle', 'owner', 'description', 'entry_date','departure_date', 'final_price', 'status']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Sacamos el usuario de los argumentos
        super(billingForm, self).__init__(*args, **kwargs)

        self.fields['vehicle'].queryset = Vehicles.objects.filter(user=user)
        self.fields['owner'].queryset = Clients.objects.filter(user=user)
    