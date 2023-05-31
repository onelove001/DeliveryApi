from django.urls import path
from  .views import *

app_name="auth"

urlpatterns = [
    path("", HelloView.as_view(), name="hello-view"),
    path("signup", UserCreateView.as_view(), name="sign-up"),
    
]