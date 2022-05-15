from django.urls import URLPattern, path
from authentication.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup_view'),
]