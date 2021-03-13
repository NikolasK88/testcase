from rest_framework import routers
from alias.views import AliasView

router = routers.DefaultRouter()
router.register('alias', AliasView, 'alias')

urlpatterns = router.urls