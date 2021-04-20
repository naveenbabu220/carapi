from django.urls import path
from . import views
urlpatterns = [
    path('GET/api/car/', views.car_get, name = 'get'),
    path('POST/api/car/', views.car_post, name = 'post'),
    path('GET/api/car<int:id>', views.car_get_car, name = 'get_car'),
]