from django.urls import include, path
from rest_framework import routers

from anagram.views import WordViewSet


router = routers.DefaultRouter()
router.register(r"words", WordViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
