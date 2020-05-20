from rest_framework import serializers
from api.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    """
        InventorySerializer inherits ModelSerializer. This ModelSerializer
        will perform all necessary operations like insert, update, select,
        delete.
    """

    class Meta:
        model = Inventory
        exclude = ('audit_status',)
