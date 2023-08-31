from django.urls import path
from .views import indexPageView, analystPageView, dunkerPageView, sideprojectPageView, threeDPageView

urlpatterns = [
    path('', indexPageView, name = "index"),
    path('analyst/', analystPageView, name = "analyst"),
    path('dunker/', dunkerPageView, name = "dunker"),
    path('sideprojects/', sideprojectPageView, name = "sideprojects"),
    path('3D/', threeDPageView, name = "threeD"),

]