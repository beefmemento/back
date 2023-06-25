from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

from django.urls import path
from .views import PostBySubjectView

urlpatterns = [
    path('posts/<str:subject_title>/', PostBySubjectView.as_view(), name='post-by-subject'),
    # 다른 url 패턴들...
]
urlpatterns += router.urls

