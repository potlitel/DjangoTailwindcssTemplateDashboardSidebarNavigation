from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="home"),
    path("/products", views.products, name="products"),
    ]