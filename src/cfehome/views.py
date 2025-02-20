from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse
# import logging


# logger = logging.getLogger(__name__)

def home_page_view_v1(request):
    return HttpResponse("<h1>Hello, world. You're at the cfehome index.</h1>")

def home_page_view_v2(request):
    return render(request, 'example_home_pages/home.html')

def dynamic_page_view_v1(request):
    context = {
        'title': 'Welcome to My Fun Page!',
        'message': 'Enjoy your stay and have fun!',
        'items': ['Django', 'Python', 'HTML', 'CSS', 'JavaScript'],
        'user': {'name': 'Aman', 'age': 28}
    }
    return render(request, 'example_home_pages/dynamic1.html', context)

def home_page_view(request):
    # logger.info("Home page view accessed")
    # logger.debug("Debugging home page view")
    return render(request, 'pages/home.html')

@login_required
def about_page_view(request):
    return render(request, 'pages/about.html')

# Override the Default Logout View
def custom_logout(request):
    logout(request)  # Log the user out
    return redirect(reverse('account_login'))  # Redirect to the login page