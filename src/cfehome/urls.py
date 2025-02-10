"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import home_page_view_v1, home_page_view_v2, dynamic_page_view_v1, home_page_view, about_page_view, custom_logout
from django.shortcuts import redirect

# Redirect to login page
def home_redirect(request):
    return redirect("account_login")

urlpatterns = [
    
        # Note : To use below commented routes in settings.py uncomment the following line
        # 'DIRS': [BASE_DIR / "cfehome" / "templates"],
        
        # path('home/', include([
        #     path('v1/', home_page_view_v1),
        #     path('v2/', home_page_view_v2),
        # ])),
        
        # path('dynamic/', include([
        #     path('v1/', dynamic_page_view_v1),
        # ])),
       
       
        # Note : To use below commented routes in settings.py uncomment the following line
        # 'DIRS': [BASE_DIR / "templates"],

        # path('/', home_page_view, name='home'),
        path('', home_redirect),
        path('home', home_page_view, name='home'),
        path('about/', about_page_view, name='about'),
        
        # Override Allauth's logout
        path('accounts/logout/', custom_logout, name='account_logout'),  
        
        #Apps routes
        path('profiles/', include('profiles.urls')),
        
        # Allauth routes
        path('accounts/', include('allauth.urls')),

        #admin
        path('admin/', admin.site.urls),
]
