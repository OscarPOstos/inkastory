from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet, StoryNodeListCreateView, StoryNodeDetailView, StoryStartView, StoryProgressView

router = DefaultRouter()
router.register(r'stories', StoryViewSet, basename='story')

urlpatterns = [
    path('', include(router.urls)),
    path('stories/<int:story_id>/nodes/', StoryNodeListCreateView.as_view(), name='story-node-list-create'),
    path('nodes/<int:pk>/', StoryNodeDetailView.as_view(), name='story-node-detail'),
    path('stories/<int:story_id>/start/', StoryStartView.as_view(), name='story-start'),
    path('stories/<int:story_id>/progress/', StoryProgressView.as_view(), name='story-progress'),
]