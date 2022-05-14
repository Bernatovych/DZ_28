from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated
from news.models import News, WebsiteSettings
from .serializers import NewsSerializer, WebsiteSettingsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters


class NewsListView(ListAPIView):
    """
        Return a list of all the existing news(10 news for page).
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]


class WebsiteSettingsList(APIView):
    """
        get:
            Return a list of all website to parse.

        post:
            Create a new website to parse.
    """

    def get(self, request, format=None):
        sites = WebsiteSettings.objects.all()
        serializer = WebsiteSettingsSerializer(sites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WebsiteSettingsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WebsiteSettingsDetail(APIView):
    """
        get:
            Return the given website.

        put:
            Edit the given website.

        delete:
            Delete the given website.
    """

    def get(self, request, pk, format=None):
        site = get_object_or_404(WebsiteSettings, pk=pk)
        serializer = WebsiteSettingsSerializer(site)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        site = get_object_or_404(WebsiteSettings, pk=pk)
        serializer = WebsiteSettingsSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        site = get_object_or_404(WebsiteSettings, pk=pk)
        site.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)