from django.urls import URLPattern, path
from authentication.views import SignUpView, home

urlpatterns = [
    path('', home, name='home_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
]