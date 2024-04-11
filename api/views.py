from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models import Books, Members
from .serializers import BookSerialzier, MemberSerializer

# Create your views here.
class BookViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerialzier
    # permission_classes = [permissions.IsAuthenticated]

class MemberViewset(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer


class OrderViewset(viewsets.ViewSet):

    @action(detail=True, methods=["post"], url_path="checkout")
    def checkout(self, request):
        return Response("checkout", status=201)

    @action(detail=True, methods=["post"], url_path="return_request")
    def return_request(self, request):
        return Response("return request", status=200)
