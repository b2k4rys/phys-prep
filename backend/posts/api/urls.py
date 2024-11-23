from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import PostViewSet
# post_router = DefaultRouter()
# post_router.register(r"posts", PostListAPIView)


from .views import PostListAPIView

urlpatterns = [path("posts/<int:section>/<int:set>/", PostListAPIView.as_view())]
