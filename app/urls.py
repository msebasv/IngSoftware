from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('send-email/', views.send_email, name='create_email'),
    path('email-sent/', views.send_email, name='sent_email'),
    

]

