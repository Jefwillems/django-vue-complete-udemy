from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from quotesapi.serializers import QuoteSerializer
from quotesapi.models import Quote
from . import permissions

# Create your views here.


class QuoteDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
    permission_classes = [permissions.IsAdminOrReadOnly]


class QuoteView(ListCreateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
    permission_classes = [permissions.IsAdminOrReadOnly]
