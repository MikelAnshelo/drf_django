from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/Projectos',ProjectViewSet,'Projectos')

urlpatterns = router.urls