"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from squad.views import *

from post.views import *

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('squad/', index), # http://127.0.0.1:8000/squad/
    # path('', index), # http://127.0.0.1:8000
    # path('cont/', contact), # http://127.0.0.1:8000/cont/
    # path('squad/', include('squad.urls')),
    path('', include('squad.urls')),  # http://127.0.0.1:8000
    # path('post/', home),
    # path('categ/', categories),
    path("post/", include('post.urls')),

]


handler404 = pageNotFound