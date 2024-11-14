from rest_framework import generics, mixins
from .models import User
from .serializers import UserSerializer

class UserListCreateView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs, partial=True)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
