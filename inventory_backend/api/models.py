from __future__ import unicode_literals

import uuid
from django.db import models
from decimal import Decimal
from django.core.validators import (MinLengthValidator, MinValueValidator)


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)],
                            help_text='Name of Inventory')
    description = models.CharField(max_length=1440,
                                   help_text='Inventory description')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, help_text='Price of the Inventory',
        validators=[MinValueValidator(Decimal('0.50'))])
