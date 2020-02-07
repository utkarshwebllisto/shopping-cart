from django.shortcuts import render
from rest_framework import viewsets
from rental import models
from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = BelongingSerializer


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = BorrowedSerializer