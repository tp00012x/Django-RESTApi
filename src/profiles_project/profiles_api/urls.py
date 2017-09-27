from django.conf.urls import url, include
from .views import HelloApiView, HelloViewSet

from rest_framework.routers import DefaultRouter

app_name = 'profiles_api'
router = DefaultRouter()
router.register('hell-viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    url(r'^hello-view/', HelloApiView.as_view()),
    url(r'', include(router.urls))
]