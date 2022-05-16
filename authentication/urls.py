from django.urls import URLPattern, path
from authentication.views import (
    SignInView,
    SignUpView,
    home
    )

urlpatterns = [
    path('', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
]