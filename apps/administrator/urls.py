from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreateAct, ListAct, viewDataProfile

urlpatterns = [
    path('new_act/', login_required(CreateAct.as_view()), name="new_act"),
    path('list_act/', login_required(ListAct.as_view()), name="list_act"),
    path('profile/',login_required(viewDataProfile.as_view()), name="profile")
]

