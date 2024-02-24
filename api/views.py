from django.shortcuts import render
from django.contrib.auth import authenticate

from .serializers import *
from app.models import *
from accounts.tokens import create_jwt_pair_for_user

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "User created successfully",
                "data": serializer.data
            }        

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)

            response = {
                "message": "Login successful",
                "tokens": tokens
            }

            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request: Request):        

        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }

        return Response(data=content, status=status.HTTP_200_OK)


class SliderViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class WhyChooseUsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WhyChooseUs.objects.all()
    serializer_class = WhyChooseUsSerializer


class HealthySectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HealthySection.objects.all()
    serializer_class = HealthySectionSerializer


class TrainerSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TrainerSection.objects.all()
    serializer_class = TrainerSectionSerializer


class ContactSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class InfoSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = InfoSection.objects.all()
    serializer_class = InfoSectionSerializer