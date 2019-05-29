from fetch import views
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home, name="home"),
]