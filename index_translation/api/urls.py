from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import cooperativeViewSet, corridorViewSet, routaViewSet

router = DefaultRouter()
router.register('cooperative', cooperativeViewSet, basename='cooperative')
router.register('corridor', corridorViewSet, basename='corridor')
router.register('routa', routaViewSet, basename='routa')

urlpatterns = [
    url('', include(router.urls)),
    #path('corridor/',corridor_upload_file_view, name='corridor-view'),
]
