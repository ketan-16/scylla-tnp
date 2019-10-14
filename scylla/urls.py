"""scylla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from users import views as usviv
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('blog.urls')),
    path('register/', include('users.urls')),
    path('dashboard/', usviv.dashboard, name='dashboard'),
    path('update_profile/', usviv.update_profile, name='update-profile'),
    path('stats/', usviv.stats, name='stats'),
    path('export/', usviv.export, name='export'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path(r'^export/csv/$', usviv.export, name='export'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)