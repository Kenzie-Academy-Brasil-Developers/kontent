from calendar import c
from pyexpat import model
from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict

from content.validator import ContentValidator

from .models import Content
from . import views
import content
# Create your views here.


class ContentView(APIView):
    def get(self, request: Request) -> Response:
        contents = Content.objects.all()
        contents_list = [model_to_dict(content) for content in contents]
        return Response(contents_list)

    def post(self, request: Request) -> Response:
        try:
            content_validated = ContentValidator(**request.data)
            print(content_validated)
            if content_validated.is_valid() == True:
                content = Content.objects.create(**request.data)
                content_dict = model_to_dict(content)
                return Response(content_dict, status.HTTP_201_CREATED)
            raise KeyError
        except KeyError:
            return Response({"details": content_validated.errors}, status.HTTP_400_BAD_REQUEST)


class ContentDetails(APIView):
    def get(self, request: Request, content_id: int) -> Response:
        try:
            content = Content.objects.get(id=content_id)
            content_dict = model_to_dict(content)
            return Response(content_dict)
        except Content.DoesNotExist:
            return Response({"detail": "Content not found"}, status.HTTP_404_NOT_FOUND)
            ...

    def patch(self, request: Request, content_id: int) -> Response:
        try:
            content = Content.objects.get(id=content_id)

            for key, value in request.data.items():
                setattr(content, key, value)

            content.save()
            content_dict = model_to_dict(content)
            return Response(content_dict)

        except Content.DoesNotExist:
            return Response({"detail": "Content not found"}, status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, content_id: int) -> Response:
        try:
            content = Content.objects.get(id=content_id)
            content.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Content.DoesNotExist:
            return Response({"detail": "Content not found"}, status.HTTP_404_NOT_FOUND)


class ContentFilter(APIView):
    def get(self, request: Request) -> Response:
        try:
            title = request.query_params.get('title', None)

            content = Content.objects.filter(title__iexact=title)
            content_list = [model_to_dict(content) for content in content]
            if len(content_list) == 0:
                raise Content.DoesNotExist
            return Response(content_list)
        except Content.DoesNotExist:
            return Response({"details": "Title not found"}, status.HTTP_404_NOT_FOUND)
