# Generated by Django 2.1.3 on 2020-05-19 15:38

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of Inventory', max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.CharField(help_text='Inventory description', max_length=1440)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price of the Inventory', max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.50'))])),
            ],
        ),
    ]
