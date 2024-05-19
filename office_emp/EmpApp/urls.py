from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('allview/',views.ViewEmp),
    path('addemp/',views.AddEmp),
    path('remove/',views.Remove),
    path('filter/',views.Filters),

]
