"""Users views."""

#API
from rest_framework import generics
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from users.models import Profile

#API
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

#generics.ListCreateAPIView






        
    

