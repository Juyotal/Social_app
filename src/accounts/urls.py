from django.conf.urls import url
from . import views
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'accounts'

urlpatterns = [
    url(r"login/$", LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r"logout/$", LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),

]

