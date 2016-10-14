from rest_framework import generics

from users.serializers import *
from users.models import User


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
