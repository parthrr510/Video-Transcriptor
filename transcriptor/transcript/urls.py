from django.urls import path
from . import views
app_name = "transcript"


urlpatterns = [
    path('',views.home,name = 'home'),
]