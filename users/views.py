from rest_framework.decorators import detail_route, parser_classes
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, viewsets
from users.serializers import UserSerializer, GroupSerializer, UserProfileSerializer
from .models import UserProfile
from rest_framework.test import APIRequestFactory

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @detail_route(methods=['POST'])
    @parser_classes((FormParser, MultiPartParser,))
    def image(self, request, *args, **kwargs):
        if 'upload' in request.data:
            user_profile = self.get_object()

            user_profile.image.delete()

            upload = request.data['upload']

            user_profile.image.save(upload.name, upload)

            return Response(status=HTTP_201_CREATED, headers={'Location': user_profile.image.url})
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class UserProfileMultiPartParserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @parser_classes((MultiPartParser,))
    def update(self, request, *args, **kwargs):
        if 'upload' in request.data:
            user_profile = self.get_object()

            user_profile.image.delete()

            upload = request.data['upload']

            user_profile.image.save(upload.name, upload)

        return super(UserProfileMultiPartParserViewSet, self).update(request, *args, **kwargs)