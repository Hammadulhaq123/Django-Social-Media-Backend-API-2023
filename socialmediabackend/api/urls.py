from rest_framework.routers import DefaultRouter
from users.views import UserViewset
from user_profile.views import UserProfileView
from posts.views import PostsViewset
from comments.views import CommentsViewset
from likes.views import LikesViewset

router = DefaultRouter()
router.register(r'users', UserViewset, basename='users')
router.register(r'profiles', UserProfileView, basename='profiles')
router.register(r'posts', PostsViewset, basename='posts')
router.register(r'comments', CommentsViewset, basename='comments')
router.register(r'likes', LikesViewset, basename='likes')
urlpatterns = router.urls
