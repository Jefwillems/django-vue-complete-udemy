from django.urls import path
from .views import QuoteDetailView, QuoteView

urlpatterns = [
    path('quote/', QuoteView.as_view(), name='quote-list'),
    path('quote/<int:pk>', QuoteDetailView.as_view(), name='quote-detail')
]
