from django.contrib import admin
from django.urls import path
from microservice1 import views


urlpatterns = [
    path('', views.home),
    path('adoptions/<int:id>', views.pet_detail, name='pet_detail'),
    path('pets', views.all_pets),
    path('admin/', admin.site.urls),
]
