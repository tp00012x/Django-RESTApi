from django.conf.urls import url
from .views import HelloApiView

app_name = 'profiles_api'

urlpatterns = [
    url(r'^hello-view/', HelloApiView.as_view()),
]