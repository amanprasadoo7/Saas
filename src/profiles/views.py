from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def profile_view(request, username):
    
    # try:
    #     user = User.objects.get(username=username)
    #     return HttpResponse(f'<h1>Hello, {username}. You\'re at the cfehome index. Your ID is {user.id}</h1>')
    # except User.DoesNotExist:
    #     return HttpResponse('<h1>Invalid username</h1>')
    # Retrieve the user with the given username or return a 404 if not found
    user_obj = get_object_or_404(User, username=username)
    
    # Create a context dictionary with the user object
    context = {
        'profile_user': user_obj,
    }
    
    # Render the template with the context
    return render(request, 'account/my_profile.html', context)