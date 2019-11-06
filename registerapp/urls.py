from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexView,name='index'),
    path('faq/',views.faqView,name='faq'),
    path('about/',views.aboutView,name='about'),
    path('register/',views.regView,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('dashboard/',views.dashboardView,name='dashboard'),
    
]