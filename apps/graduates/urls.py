from django.urls import path
from . import views

urlpatterns = [
    path('form_data/',views.mi_vista, name="form_data"),
    path('profile/',views.mi_vista_profile, name="profile")

]

