from rest_framework import APIView, Request, Response, status

from . import views
# Create your views here.


class ContentView(APIView):
    def get(self, request: Request) -> Response:
        ...

    def post(self, request: Request) -> Response:
        ...
