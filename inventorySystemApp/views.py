from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password are wrong.')

    return render(request, 'inventorySystemApp/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created!")
            return redirect('login')
        else:
            messages.error(request, "Error")
    else:
        form = UserCreationForm()

    return render(request, 'inventorySystemApp/register.html', {'form': form})

def home(request):

    return render(request, "inventorySystemApp/home.html")

def discussions(request):
    return render(request, 'inventorySystemApp/discussions.html')

def questions(request):
    return render(request, 'inventorySystemApp/questions.html')

def about(request):
    return render(request, 'inventorySystemApp/about.html')


def receiving_items(request):

    return render(request, "inventorySystemApp/receivinf.html")


# def inventory_management(request):

    # return render(request, "inventorySystemApp/inventory.html")




def send_items(request):

    return render(request, "inventorySystemApp/outbound.html")

def dashboard(request):

    return render(request, "inventorySystemApp/dashboard_info.html")