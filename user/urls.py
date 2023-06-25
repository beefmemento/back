# from django.urls import path, include
# from rest_framework import routers
# from .views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     #path('login/', LoginView.as_view(), name='login'),
# 

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DefaultUserViewSet, SubjectViewSet, UserToSubjectViewSet

router = DefaultRouter()
router.register(r'users', DefaultUserViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'user_subjects', UserToSubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

