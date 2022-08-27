from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import *
from .permissions import IsAdminOrReadOnly
from .serializers import FilmsSerializer, MemberSerializer, FilmSerializer, CommentSerializer, MemberPreviewSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmsSerializer
    lookup_field = 'pk'

    permission_classes = (IsAdminOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = FilmSerializer
        self.queryset = Film.objects.all().prefetch_related('genre', 'actors', 'directors',
                                                            'operators', 'writers',
                                                            'producers')
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def member(self, request, pk=None):
        if request.method == 'GET':
            self.serializer_class = MemberSerializer
            instance = Member.objects.get(pk=pk)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    @action(methods=['get', 'post'], detail=True, permission_classes=(IsAuthenticatedOrReadOnly,))
    def comments(self, request, pk=None):
        self.serializer_class = CommentSerializer
        if request.method == 'GET':
            instance = Comment.objects.filter(film__id=pk)
            serializer = self.get_serializer(instance, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                comment = Comment.objects.create(
                    user=User.objects.get(pk=serializers.CurrentUserDefault().requires_context
                                        ),
                    content=serializer.validated_data['content'],
                    film=Film.objects.get(pk=pk)
                )
                comment.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(400, status=status.HTTP_400_BAD_REQUEST)
