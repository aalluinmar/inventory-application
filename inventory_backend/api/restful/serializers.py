import logging

from rest_framework import serializers
from api.models import Inventory

from api.services.utils import check_alpha_exists

# Get an instance of a logger
logger = logging.getLogger(__name__)


class InventorySerializer(serializers.ModelSerializer):
    """
        InventorySerializer inherits ModelSerializer. This ModelSerializer
        will perform all necessary operations like insert, update, select,
        delete.
    """

    def validation_name(self, data):
        if not check_alpha_exists(data):
            msg = ("Name `{0}` must contain atleast one letter".format(data))
            logger.error(msg)
            raise serializers.ValidationError(msg)
        return data

    class Meta:
        model = Inventory
        exclude = ('audit_status',)
