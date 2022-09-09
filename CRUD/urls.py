from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name="Home"),
    path('delete/<int:id>/', views.Delete_Data, name="delete_data"),
    path('/<int:id>/', views.Update_Data, name="update_data"),
]
