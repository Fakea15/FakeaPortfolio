from django.urls import path
from . import views
from .views import RequestView, ContactView

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about_me/', views.AboutView, name='about'),
    path('request/', RequestView.as_view(), name='request'),
    path('where_the_happen/', views.PortfolioView, name='portfolio')
]



