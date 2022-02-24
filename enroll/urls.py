from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('face/', views.face, name='face'),
    path('detail/', views.detail, name='detail'),
    path('student/', views.student, name='student'),
]
