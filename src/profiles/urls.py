from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import profile_view

urlpatterns = [

    path('<username>/', profile_view, name='profile'),
    
]
