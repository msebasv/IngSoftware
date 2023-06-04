from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import viewDataProfile, results

urlpatterns = [
    path('profile/',login_required(viewDataProfile.as_view()), name="profile"),
    path('results/',login_required(results.as_view()), name="results"),
    
]