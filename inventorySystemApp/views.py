from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm 
from .models import Discussion, Comment
from .forms import DiscussionForm
from .forms import CommentForm
from django.contrib.auth.decorators import login_required




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

def discussion_detail(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    comments = discussion.comments.all()

    if request.method == 'POST':  # This handles the comment submission
        content = request.POST.get('content')
        if content:
            # Create a new comment linked to the discussion and current user
            Comment.objects.create(discussion=discussion, user=request.user, content=content)
        return redirect('discussion_detail', pk=discussion.pk)  # Reload page after comment is added

    return render(request, 'inventorySystemApp/discussion_detail.html', {
        'discussion': discussion,
        'comments': comments,
    })

def discussion_create(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            
            discussion = form.save(commit=False)
            discussion.user = request.user  # Associate the discussion with the logged-in user
            discussion.save()
            return redirect('discussion_detail', pk=discussion.pk)  # This should redirect to the discussion detail page
    else:
        form = DiscussionForm()
    return render(request, 'inventorySystemApp/discussion_create.html', {'form': form})

# View to delete a discussion
@login_required
def delete_discussion(request, id):
    discussion = get_object_or_404(Discussion, id=id, user=request.user)
    
    if request.method == 'POST':
        discussion.delete()
        return redirect('discussions')  # Redirect to the discussions page after deletion
    
# View to delete a comment
@login_required
def delete_comment(request, pk):
    # Retrieve the comment to be deleted
    comment = get_object_or_404(Comment, pk=pk)
    discussion = comment.discussion  # Get the related discussion

    # Delete the comment
    comment.delete()

    # Redirect to the discussion detail page using the pk of the discussion
    return redirect('discussion_detail', pk=discussion.pk)  # Pass pk, not the entire object

def some_view(request):
    if request.user.is_authenticated:
        print(f"Logged in as: {request.user.username}")
    else:
        print("No user is logged in.")