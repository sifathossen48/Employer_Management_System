from rest_framework import generics, permissions
from .models import Employer
from .serializers import EmployerSerializer
from accounts.permissions import IsOwner

class EmployerCreateListView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Employer.objects.all()
