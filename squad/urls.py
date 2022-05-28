from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index), # http://127.0.0.1:8000/squad/
    path('', index, name = 'main'), # http://127.0.0.1:8000
    # path('cont/', contact), #http://127.0.0.1:8000/cont /
    # path('cont/<int:contid>/', contact),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('about/', about, name = 'about')

]