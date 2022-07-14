from django.urls import path
from .views import getProfiles, index, create


urlpatterns = [
    path('', index,name='index'),
    path('getProfiles', getProfiles, name='getProfiles'),
    path('create', create, name='create'),
]