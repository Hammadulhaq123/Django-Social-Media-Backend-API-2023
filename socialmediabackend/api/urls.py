from rest_framework.routers import DefaultRouter
from users.views import UserViewset
from user_profile.views import UserProfileView


router = DefaultRouter()
router.register(r'users', UserViewset, basename='users')
router.register(r'profiles', UserProfileView, basename='profiles')
urlpatterns = router.urls
