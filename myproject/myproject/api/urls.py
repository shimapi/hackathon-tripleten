from rest_framework.routers import DefaultRouter
from posts.api.urls import post_router
from django.urls import path, include

routers = DefaultRouter()

routers.registry.extend(post_router.registry)

urlpatterns = [
    path('', include(routers.urls))
]