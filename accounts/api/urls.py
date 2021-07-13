from django.urls import path, include

from .views import UserCreate, HomeView, get_csrf, login_view, logout_view, session_view, whoami_view


urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
    path('hello/', HomeView.as_view(), name='hello'),

    path('user/create/', UserCreate.as_view(), name="create_user"),

    path('csrf/', get_csrf, name='api-csrf'),
    path('login/', login_view, name='api-login'),
    path('logout/', logout_view, name='api-logout'),
    path('session/', session_view, name='api-session'),
    path('whoami/', whoami_view, name='api-whoami'),
]
