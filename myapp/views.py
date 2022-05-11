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


# viewsets with filtered views:

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'username', 'location__city', 'location__state', 'location__zipcode']
    """
    ^ Allows a User view searching by username, name, or loation (foriegn key relation to the city,state, and zipcode)
    ex: /users/?first_name=Blair
    ex: /users/?location__city=Lexington
    """

class DogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'breed__name', 'size__label', 'gender__label' ]
    """
    ^ Allows a Dog view searching by dog name, breed name, size, and gender
    """

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['dog__name']
    """
    ^ Allows a Image view searching by dog name 
    """

class ConnectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['dog_initializer__name', 'dog_target__name']
    """
    ^ Allows a Connection view searching by eithr dog name bc of the foreign key relation with the dog class
    """

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['dog_creator__name', 'dog_other__name']
    authentication_classes = ()
    """
    ^ Allows a Conversation view searching by either dog name bc of the foreign key relation with dog class
    """

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['conversation', 'dog_sent__name', 'dog_received__name']
    """
    ^ Allows a Message view searching by conversation or by the dogs involved
    """

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user__name']
    """
    ^ Allows a Comment view searching by user name bc of the foreign key relation with the user class
    """

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)