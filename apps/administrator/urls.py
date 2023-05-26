from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreateAct, ListAct

urlpatterns = [
    path('new_act/', login_required(CreateAct.as_view()), name="new_act"),
    path('list_act/', login_required(ListAct.as_view()), name="list_act"),
]