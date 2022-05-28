from django.urls import path

from post.views import *

urlpatterns = [
    path('', post_page, name = 'home'),
    path('add_post/',add, name = 'add_post'),
    path('del_post/',delete, name = 'del_post'),

]