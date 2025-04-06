from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm 
from .models import Discussion
from .forms import DiscussionForm




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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Your account has been created!")
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, "")
    else:
        form = CustomUserCreationForm()

    return render(request, 'inventorySystemApp/register.html', {'form': form})

def home(request):

    return render(request, "inventorySystemApp/home.html")

# def discussions(request):
    # return render(request, 'inventorySystemApp/discussions.html')

def questions(request):
    return render(request, 'inventorySystemApp/questions.html')

def about(request):
    return render(request, 'inventorySystemApp/about.html')


def receiving_items(request):

    return render(request, "inventorySystemApp/receiving.html")


# View to show all discussions
def discussions(request):
    discussions = Discussion.objects.all().order_by('-id')  # Sort by the latest discussions
    return render(request, 'inventorySystemApp/discussions.html', {'discussions': discussions})

# View to show a single discussion
def discussion_detail(request, id):
    discussion = get_object_or_404(Discussion, id=id)
    return render(request, 'inventorySystemApp/discussion_detail.html', {'discussion': discussion})

# View to create a new discussion
def discussion_create(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discussions')  # Redirect to the list of discussions
    else:
        form = DiscussionForm()
    return render(request, 'inventorySystemApp/discussion_create.html', {'form': form})

# View to delete a discussion
def discussion_delete(request, id):
    discussion = get_object_or_404(Discussion, id=id)
    discussion.delete()
    return redirect('discussions')  # Redirect to the list of discussions



def send_items(request):

    return render(request, "inventorySystemApp/outbound.html")

def dashboard(request):

    return render(request, "inventorySystemApp/dashboard_info.html")