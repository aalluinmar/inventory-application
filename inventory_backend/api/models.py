from __future__ import unicode_literals

import uuid
from django.db import models
from decimal import Decimal
from django.core.validators import (MinLengthValidator, MinValueValidator)
from django.core.exceptions import ValidationError

from api.services.constants import Variables
from api.services.utils import image_validation


def validate_image(image):
    """
        1. Checks the image file with Dimensions, Size and Extensions.
        2. If the data doesn't match, then it will raise validation error.
    """
    msg = image_validation(image)
    if msg:
        raise ValidationError(msg)


class Audit(models.Model):
    # Audit Details
    """
    An abstract base class model that provides self updating ``created``
    and ``modified`` fields.
    """
    audit_status = models.CharField(
        choices=Variables.audit_status, max_length=10, default='active',
        help_text='Active or InActive')
    created_on = models.DateTimeField(
        auto_now_add=True, help_text='On which date field is created')
    modified_on = models.DateTimeField(
        auto_now=True, help_text='On which date field is modified')

    class Meta:
        abstract = True


class Inventory(Audit):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)],
                            help_text='Name of Inventory')
    description = models.CharField(max_length=1440,
                                   help_text='Inventory description')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, help_text='Price of the Inventory',
        validators=[MinValueValidator(Decimal('0.50'))])
    image = models.ImageField(
        upload_to='media/', validators=[validate_image],
        help_text='Image Field for the Inventory')
