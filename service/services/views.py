from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Subscription
from .serializers import SubscriptionSerializer
from django.db.models import Prefetch
from clients.models import Client


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.select_related(
        "client", "plan", "client__user"
    ).only("client__company_name", "client__user__email", "plan_id")
    serializer_class = SubscriptionSerializer
