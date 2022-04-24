from django.contrib import admin
from django.urls import path
from sportapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='sportapp'),
    path('index',views.index, name='sportapp'),
    path('about',views.about, name='sportapp'),
    path('club',views.club, name='sportapp'),
    path('location',views.location, name='sportapp'),
    path('contact',views.contact, name='sportapp')
    
    
]