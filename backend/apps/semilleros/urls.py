from .views import (
    SemilleroViewSet,
    # PageViewSet,
    # PageContentViewSet,
    # FooterViewSet,
    # PostViewSet,
    # BannerViewSet,
    # ItemBannerViewSet,
    # MenuViewSet,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"semilleros", SemilleroViewSet, basename="api")
urlpatterns = router.urls
