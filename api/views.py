from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Project, Skill, ContactMessage, AboutMe
from .serializers import ProjectSerializer, SkillSerializer, ContactMessageSerializer, AboutMeSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ===========================================================
# portfolio/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def projects(request):
    return render(request, 'projects.html')


def skills(request):
    return render(request, 'skills.html')


def contact(request):
    return render(request, 'contact.html')


def about_me(request):
    return render(request, 'about_me.html')

def hello_me(request):
    return render(request, 'hello.html')


