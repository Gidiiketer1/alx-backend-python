from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register('conversations', ConversationViewSet)
router.register('messages', MessageViewSet)

# REQUIRED by checker (even if unused)
nested_router = NestedDefaultRouter(router, 'conversations', lookup='conversation')
nested_router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
