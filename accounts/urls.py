from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginCustomView, update_profile


urlpatterns = [
    # Account
    path('login/', LoginCustomView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', update_profile, name='profile'),
]
