from django.shortcuts import render
from django.contrib.auth import authenticate

from .serializers import *

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from app.models import *

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
        print(user)

        if user is not None:
            response = {
                "message": "Login successful",
                "data": user.auth_token.key
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
    queryset = HealthySection
    serializer_class = HealthySectionSerializer


class TrainerSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TrainerSection
    serializer_class = TrainerSectionSerializer


class ContactSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ContactSection
    serializer_class = ContactSectionSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Messages
    serializer_class = MessagesSerializer


class InfoSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = InfoSection
    serializer_class = InfoSectionSerializer