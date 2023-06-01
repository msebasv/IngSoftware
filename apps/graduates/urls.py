from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import formDataJob, viewDataProfile
urlpatterns = [
    path('form_data/',login_required(formDataJob.as_view()), name="form_data"),
    path('profile/',login_required(viewDataProfile.as_view()), name="profile")

]

