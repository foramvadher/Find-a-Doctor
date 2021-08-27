from .views import DoctorsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctor', DoctorsViewSet)
urlpatterns = router.urls
