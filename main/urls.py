from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="home"),
    path("products/", views.products, name="products"),
    path("products/", views.products, name="products"),
    path("reports/", views.reports, name="reports"),
    path("messages/", views.messages, name="messages"),
    path("calendar/", views.calendar, name="calendar"),
    path("table/", views.table, name="table"),
    path("uicomponents/", views.components, name="components"),
    path("users/", views.users, name="users"),
    ]