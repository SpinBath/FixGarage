
import json

from django.http import HttpResponse, JsonResponse
from django.utils.translation import gettext as _
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Clients, Vehicles, Services, Billing
from .forms import clientForm, vehicleForm, servicesForm, billingForm



# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'user_templates/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("/") 
            except IntegrityError:
                return render(request, 'user_templates/signup.html', {"form": UserCreationForm, "error": "Username already exists."})
        return render(request, 'user_templates/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    

def signin(request):
    if request.method == 'GET':
        return render(request, 'user_templates/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user_templates/signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('/')
        

        
@login_required
def signout(request):
    logout(request)
    return redirect('/signin')

@login_required 
def index(request):
    return render(request, 'container_templates/index.html')

@login_required                             
def clients(request):

    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            clients = Clients.objects.filter(user=request.user).filter(Q(name__icontains=query) | Q(address__icontains=query)| Q(phone__icontains=query)| Q(email__icontains=query))

        else:
            clients = Clients.objects.filter(user=request.user)

        return render(request, 'container_templates/clients.html', {'clients': clients, 'form': clientForm(), 'query': query})
    else:
        Clients.objects.create(
            user = request.user,
            name=request.POST['name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            email=request.POST['email']
        )
        return redirect('/clients')

@login_required 
def deleteclient(request, id):  
    client = get_object_or_404(Clients, id=id)  
    client.delete()  
    return redirect("/clients") 


@login_required 
def updateclient(request, id):
    client = get_object_or_404(Clients, id=id)
    if request.method == 'POST':
        form = clientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/clients')
    else:
        form = clientForm(instance=client)
    return render(request, 'container_templates/clients.html', {'form': form, 'is_update': True})


@login_required 
def vehicles(request):

    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            vehicles = Vehicles.objects.filter(user=request.user).filter(Q(owner__name__icontains=query) | Q(brand__icontains=query) | Q(model__icontains=query) | Q(year__icontains=query) | Q(license_plate__icontains=query))

        else:
            vehicles = Vehicles.objects.filter(user=request.user)

        return render(request, 'container_templates/vehicles.html', {'vehicles': vehicles, 'form': vehicleForm(user=request.user), 'query':query})

    else:
        client = get_object_or_404(Clients, id=request.POST['owner'])
        Vehicles.objects.create(
            user = request.user,
            owner=client,
            brand=request.POST['brand'],
            model=request.POST['model'],
            year=request.POST['year'],
            license_plate=request.POST['license_plate']
        )
        return redirect('/vehicles')
    
@login_required 
def deletevehicle(request, id):  
    vehicle = get_object_or_404(Vehicles, id=id)  
    vehicle.delete()  
    return redirect("/vehicles") 

@login_required 
def updatevehicle(request, id):
    vehicle = get_object_or_404(Vehicles, id=id)
    if request.method == 'POST':
        form = vehicleForm(request.POST,user=request.user, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('/vehicles')
    else:
        form = vehicleForm(user=request.user, instance=vehicle)
    return render(request, 'container_templates/vehicles.html', {'form': form, 'is_update': True})



@login_required 
def services(request):

    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            if query:
          
                services = Services.objects.filter(user=request.user).filter(Q(vehicle__brand__icontains=query) | Q(vehicle__model__icontains=query) | Q(vehicle__license_plate__icontains=query) | Q(owner__name__icontains=query) | Q(description__icontains=query) | Q(entry_date__icontains=query) | Q(departure_date__icontains=query) | Q(price__icontains=query))

        else: 
            services = Services.objects.filter(user=request.user)
        
        return render(request, 'container_templates/services.html', {'services': services, 'form': servicesForm(user=request.user), 'query':query})
    else:
        vehicle_object=get_object_or_404(Vehicles, id=request.POST['vehicle'])
        owner_object=get_object_or_404(Clients, id=request.POST['owner'])

        Services.objects.create(
            user = request.user,
            vehicle = vehicle_object,
            owner = owner_object,
            description = request.POST['description'],
            entry_date = request.POST['entry_date'],
            departure_date = request.POST['departure_date'],
            price = request.POST['price'],
        )

        
        return redirect('/services')
    
@login_required 
def deleteservice(request, id):  
    service = get_object_or_404(Services, id=id)  
    service.delete()  
    return redirect("/services") 

@login_required 
def updateservice(request, id):
    service = get_object_or_404(Services, id=id)
    if request.method == 'POST':
        form = servicesForm(request.POST, user=request.user, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/services')
    else:
        form = servicesForm(user=request.user, instance=service)
    return render(request, 'container_templates/services.html', {'form': form, 'is_update': True})



@login_required 
def billing(request):

    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            billing = Billing.objects.filter(user=request.user).filter(Q(vehicle__icontains=query) | Q(owner__icontains=query) | Q(description__icontains=query) | Q(entry_date__icontains=query) | Q(departure_date__icontains=query) | Q(final_price__icontains=query))

        else: 
            billing = Billing.objects.filter(user=request.user)
        
        return render(request, 'container_templates/billing.html', {'billing': billing, 'form': billingForm(user=request.user), 'query':query, })
    else:
        vehicle_object=get_object_or_404(Vehicles, id=request.POST['vehicle'])
        owner_object=get_object_or_404(Clients, id=request.POST['owner'])

        if 'status' in request.POST:
            status = True
        else:
            status = False

        Billing.objects.create(
                user = request.user,
                vehicle=vehicle_object,
                owner=owner_object,         
                description=request.POST['description'],
                entry_date = request.POST['entry_date'],
                departure_date = request.POST['departure_date'],
                final_price=request.POST['final_price'],
                status=status,
            )
        return redirect('/billing')

@login_required
def make_billing(request, id):

    if request.method == 'GET':

        try:
            billing = Billing.objects.filter(user=request.user)

            service_obj = get_object_or_404(Services, id=id,user=request.user)
            vehicle = str(get_object_or_404(Vehicles, brand=service_obj.vehicle.brand,user=request.user).id)
            owner = str(get_object_or_404(Clients, name=service_obj.owner.name,user=request.user).id)
            description = service_obj.description
            entry_date = str(service_obj.entry_date)
            departure_date = str(service_obj.departure_date)
            final_price = str(service_obj.price)
            context = {'vehicle':vehicle ,'owner': owner , 'description':description , 'entry_date': entry_date, 'departure_date': departure_date, 'final_price': final_price}


            return render(request, 'container_templates/billing.html', {'billing': billing, 'form': billingForm(user=request.user),'context_json': json.dumps(context), 'is_update': True})
        except Services.DoesNotExist:
            return JsonResponse({'owner': ''}, status=404)
        
    else:

        vehicle_object=get_object_or_404(Vehicles, id=request.POST['vehicle'])
        owner_object=get_object_or_404(Clients, id=request.POST['owner'])

        if 'status' in request.POST:
            status = True
        else:
            status = False

        Billing.objects.create(
                user = request.user,
                vehicle=vehicle_object,
                owner=owner_object,         
                description=request.POST['description'],
                entry_date = request.POST['entry_date'],
                departure_date = request.POST['departure_date'],
                final_price=request.POST['final_price'],
                status=status,
            )
        return redirect('/billing')
    
@login_required 
def deletebilling(request, id):  
    billing = get_object_or_404(Billing, id=id)  
    billing.delete()  
    return redirect("/billing") 

@login_required 
def updatebilling(request, id):
    billing = get_object_or_404(Billing, id=id)
    if request.method == 'POST':
        form = billingForm(request.POST,user=request.user, instance=billing)
        if form.is_valid():
            form.save()
            return redirect('/billing')
    else:
        form = billingForm(user=request.user, instance=billing)
    return render(request, 'container_templates/billing.html', {'form': form, 'is_update': True})





def get_owner(request, id):

    if id:
        try:
            vehicle = get_object_or_404(Vehicles, id=id)
            owner = vehicle.owner.id
            return JsonResponse({'owner': owner})
        except Vehicles.DoesNotExist:
            return JsonResponse({'owner': ''}, status=404)
    return JsonResponse({'owner': ''}, status=400)

def get_cost(request, id):

    if id:
        try:
            service_price = get_object_or_404(Services, id=id).price
            service_description = get_object_or_404(Services, id=id).description
            return JsonResponse({'price': service_price , 'description': service_description})
        except Vehicles.DoesNotExist:
            return JsonResponse({'price': '', 'description': ''}, status=404)
    return JsonResponse({'price': '', 'description': ''}, status=400)
    
