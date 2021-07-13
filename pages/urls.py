from django.urls import path
from .views import HomeView, HomeLoggedInView


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('logged_in/', HomeLoggedInView.as_view(), name='home_page_logged_in'),
]
