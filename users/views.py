from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from users.models import Pay
from users.serializers import PaySerializer


# Create your views here.


# class PayListAPIView(generics.ListAPIView):
#     serializer_class = PaySerializer
#     queryset = Pay.objects.all()


class PayViewSet(viewsets.ModelViewSet):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['lesson', 'course', 'payment_method']
    ordering_fields = ['date']