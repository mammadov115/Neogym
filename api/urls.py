from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register("slider", views.SliderViewset, basename="slider")
router.register("why-choose-us", views.WhyChooseUsViewSet, basename="why-choose-us"),
router.register("healthy-section", views.HealthySectionViewSet, basename="healthy-section"),
router.register("trainer-section", views.TrainerSectionViewSet, basename="trainer-section"),
router.register("contact-section", views.ContactSectionViewSet, basename="contact-section"),
router.register("messages", views.MessagesViewSet, basename="messages"),
router.register("info-section", views.InfoSectionViewSet, basename="info-section"),

urlpatterns = [
    path("auth/signup/", views.SignUpView.as_view(), name="signup"),
    path("auth/login/", views.LoginView.as_view(), name="login"),
    path("auth/jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("auth/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(router.urls))
]
