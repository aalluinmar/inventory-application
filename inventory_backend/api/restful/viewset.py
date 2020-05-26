import logging

from rest_framework import viewsets

from api.restful.serializers import InventorySerializer
from api.models import Inventory

# Get an instance of a logger
logger = logging.getLogger(__name__)


class InventoryViewSet(viewsets.ModelViewSet):
    """
        Invokes ModelViewSet to perform all CRUD operations.
    """

    queryset = Inventory.objects.all().order_by('name')
    serializer_class = InventorySerializer
