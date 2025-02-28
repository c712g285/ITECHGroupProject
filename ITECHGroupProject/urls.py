"""ITECHGroupProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# chongzhi first commit demo demo
from django.contrib import admin
from django.urls import path, include
from recipeSite import views
from recipeSite import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.browseRecipe, name= 'browseRecipes'),
    path('admin/', admin.site.urls),
    path('myAccount/', views.myAccount, name= 'myAccount'),
    path('recipes/', include('recipeSite.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
