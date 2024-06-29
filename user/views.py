from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from user import models
from .serializers import UserSerializer, UserContactCreateSerializer, UserLoginSerializer, UserContactSerializer


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAdminUser]


class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'


class UserCreate(CreateAPIView):
    serializer_class = UserContactCreateSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAdminUser]


class UserContactView(ListAPIView):
    serializer_class = UserContactSerializer
    queryset = models.UserContactApplication.objects.all()
    permission_classes = [IsAdminUser]


class UserContactDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserContactSerializer
    lookup_field = 'id'
    queryset = models.UserContactApplication.objects.all()
    permission_classes = [IsAdminUser]


class UserContactCreate(CreateAPIView):
    serializer_class = UserContactSerializer
    queryset = models.UserContactApplication
    permission_classes = [IsAdminUser]


class UserLoginView(GenericAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_200_OK)


class UserLogOutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()

        return Response({'detail': "Successfully logged out"}, status=status.HTTP_204_NO_CONTENT)
