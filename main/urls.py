from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list_view/", views.listView, name="list_view"),
    # path("result/", views.result, name="result"),
    path("admin_list/", views.admin_list, name="admin_list"),
    path("admin_table/", views.admin_table, name="admin_table"),
]