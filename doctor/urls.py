from django.urls import path
from . import views
urlpatterns = [
   path('d_logout', views.d_logout, name="d_logout"),    
   path('d_dashboard', views.d_dashboard, name="d_dashboard"),       
]