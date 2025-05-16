from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Story
from .serializers import StorySerializer
from .models import StoryNode
from .serializers import StoryNodeSerializer
from rest_framework import generics
from .models import UserProgress
from .serializers import UserProgressSerializer

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

# GET /api/progress/
class UserProgressListView(generics.ListAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)

# GET, POST, DELETE /api/progress/{story_id}/
class UserProgressDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, story_id):
        progress = UserProgress.objects.filter(user=request.user, story_id=story_id).first()
        if not progress:
            return Response({'detail': 'No progress found.'}, status=404)
        serializer = UserProgressSerializer(progress)
        return Response(serializer.data)

    def post(self, request, story_id):
        node_id = request.data.get('current_node_id')
        if not node_id:
            return Response({'detail': 'Missing current_node_id.'}, status=400)

        progress, created = UserProgress.objects.update_or_create(
            user=request.user,
            story_id=story_id,
            defaults={'current_node_id': node_id}
        )
        serializer = UserProgressSerializer(progress)
        return Response(serializer.data, status=201 if created else 200)

    def delete(self, request, story_id):
        deleted, _ = UserProgress.objects.filter(user=request.user, story_id=story_id).delete()
        if deleted:
            return Response({'detail': 'Progress reset.'})
        return Response({'detail': 'No progress to delete.'}, status=404)