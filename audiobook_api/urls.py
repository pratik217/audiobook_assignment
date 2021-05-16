from django.urls import path, include

from rest_framework.routers import DefaultRouter
from audiobook_api import views


router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('song', views.SongViewSet)
router.register('pod', views.PodcastViewSet)
router.register('audio', views.AudioBookViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
