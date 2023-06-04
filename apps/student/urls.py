from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import early_Assessment, viewDataProfile
urlpatterns = [
    path('early_assessment/',login_required(early_Assessment.as_view()), name="early_Assessment"),
    path('profile/',login_required(viewDataProfile.as_view()), name="profile")

]

