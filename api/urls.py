from . import views
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()

router.register("slider", views.SliderViewset, basename="slider")
router.register("why-choose-us", views.WhyChooseUsViewSet, basename="why-choose-us"),
router.register("healthy-section", views.HealthySectionViewSet, basename="healthy-section"),
router.register("trainer-section", views.TrainerSectionViewSet, basename="trainer-section"),
router.register("contact-section", views.ContactSectionViewSet, basename="contact-section"),
router.register("messages", views.MessagesViewSet, basename="messages"),
router.register("info-section", views.InfoSectionViewSet, basename="info-section"),



urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("auth/signup/", views.SignUpView.as_view(), name="signup"),
    path("auth/login/", views.LoginView.as_view(), name="login"),
    path("auth/jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("auth/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(router.urls))
]
