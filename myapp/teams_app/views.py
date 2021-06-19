# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Teams
from .serializer import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

    lookup_field = "name"