from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('Homepage/', views.Homepage, name='Homepage'),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('signin/', views.signin, name='signin'),
]
