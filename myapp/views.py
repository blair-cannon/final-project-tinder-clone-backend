from .models import Location, Park, Breed, Gender, Socialization, Aggression, Tag, Size, User, Dog, Image, Connection, Conversation, Message, Comment
from rest_framework import status, permissions, viewsets
from .serializers import LocationSerializer, ParkSerializer, BreedSerializer, GenderSerializer, SocializationSerializer, AggressionSerializer, TagSerializer, SizeSerializer, UserSerializer, DogSerializer, ImageSerializer, ConnectionSerializer, ConversationSerializer, MessageSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ParkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

class BreedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class GenderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class SocializationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Socialization.objects.all()
    serializer_class = SocializationSerializer

class AggressionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Aggression.objects.all()
    serializer_class = AggressionSerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class SizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sizes to be viewed or edited.
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer