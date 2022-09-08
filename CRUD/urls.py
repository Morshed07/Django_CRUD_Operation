from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name="Home"),
    path('delete/<int:id>/', views.delete_data, name="Delete_data"),
]
