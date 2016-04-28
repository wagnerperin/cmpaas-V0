"""cmpaas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from users.views import UserViewSet, GroupViewSet
from maps.views import MapViewSet, MapContentViewSet, MapView, MapVersionsView
from mapper.views import MapperViewSet
from users.views import UserProfileViewSet, UserProfileMultiPartParserViewSet
from rest_framework.authtoken.views import obtain_auth_token
from authentication.views import CustomObtainAuthToken

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'maps', MapViewSet)
router.register(r'mapcontents', MapContentViewSet)
router.register(r'mapper', MapperViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'user_profiles_mpp', UserProfileMultiPartParserViewSet)

urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),
	url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/token-auth/$', CustomObtainAuthToken.as_view()),
    url(r'^api/mymaps/(?P<username>.+)/$', MapView.as_view()),
    url(r'^api/mapversions/(?P<mapId>.+)/$', MapVersionsView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)