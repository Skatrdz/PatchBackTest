from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from Api.views import PlayerViewSet, Party5ViewSet

router = routers.DefaultRouter()
router.register(r'users', PlayerViewSet)
router.register(r'party5', Party5ViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

