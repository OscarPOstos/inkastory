from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

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

# GET /api/stories/{story_id}/start/
class StoryStartView(APIView):
    def get(self, request, story_id):
        start_node = StoryNode.objects.filter(story_id=story_id, is_start=True).first()
        if not start_node:
            return Response({'detail': 'No start node found for this story.'}, status=404)
        serializer = StoryNodeSerializer(start_node)
        return Response(serializer.data)

# POST /api/stories/{story_id}/progress/
class StoryProgressView(APIView):
    def post(self, request, story_id):
        current_node_id = request.data.get('current_node_id')
        choice = request.data.get('choice')

        if not current_node_id or choice not in ['A', 'B']:
            return Response({'detail': 'Invalid request.'}, status=400)

        current_node = get_object_or_404(StoryNode, pk=current_node_id, story_id=story_id)

        next_node = None
        if choice == 'A':
            next_node = current_node.option_a_target
        elif choice == 'B':
            next_node = current_node.option_b_target

        if not next_node:
            return Response({'detail': 'No node linked to this choice.'}, status=400)

        serializer = StoryNodeSerializer(next_node)
        return Response(serializer.data)