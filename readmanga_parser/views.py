# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from readmanga_parser.queries import MangaQuery
from rest_framework.response import Response
from readmanga_parser.serializers import MangaSerializer


class SearchAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, **kwargs):
        title = kwargs.get('title')
        manga = MangaQuery().get_manga_by_title(title=title)
        manga_serializer = MangaSerializer(manga)

        return Response(manga_serializer.data)
