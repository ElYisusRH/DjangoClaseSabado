from django.urls import path 
from .views import homepageView
from .views import casapageView
urlpatterns = [
    path("", homepageView.as_view(), name = "home"),
    path("casa/", casapageView.as_view(), name = "casa")
    
]
