from django.conf.urls import url, include
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, \
    LoginViewSet, UserProfileFeedViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name='login')
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', HelloApiView.as_view()),
    url(r'', include(router.urls))
]