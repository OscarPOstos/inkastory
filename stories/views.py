from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer
from .models import StoryNode
from .serializers import StoryNodeSerializer
from rest_framework import generics

# Lista todos los nodos de una historia / Crea nodo
class StoryNodeListCreateView(generics.ListCreateAPIView):
    serializer_class = StoryNodeSerializer

    def get_queryset(self):
        story_id = self.kwargs['story_id']
        return StoryNode.objects.filter(story_id=story_id)

    def perform_create(self, serializer):
        story_id = self.kwargs['story_id']
        serializer.save(story_id=story_id)

# Detalle / Update / Delete de un nodo individual
class StoryNodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoryNode.objects.all()
    serializer_class = StoryNodeSerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer