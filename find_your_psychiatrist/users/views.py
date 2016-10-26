from rest_framework import generics

from find_your_psychiatrist.users.serializers import *
from find_your_psychiatrist.users.models import User


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
