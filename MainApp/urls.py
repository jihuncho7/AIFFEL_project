from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from .views import QuestionViewSet, CommentViewSet, SignupView, QOfMonth

router = routers.DefaultRouter()
router.register('question',QuestionViewSet)
router.register(r'question/(?P<q_id>.+)/comment',CommentViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('qofmonth/', QOfMonth.as_view(), name='qofmonth'),
]