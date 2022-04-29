from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from myapp import views
from rest_framework_simplejwt import views as jwt_views
from myapp.views import UserCreate

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'parks', views.ParkViewSet)
router.register(r'breeds', views.BreedViewSet)
router.register(r'genders', views.GenderViewSet)
router.register(r'socializations', views.SocializationViewSet)
router.register(r'aggressions', views.AggressionViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'dogs', views.DogViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'connections', views.ConnectionViewSet)
router.register(r'conversations', views.ConversationViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)