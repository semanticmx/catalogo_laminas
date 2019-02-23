import datetime
import logging

from django.conf import settings
from django.db import models

logger = logging.getLogger(__name__)


class OrderHistory(models.Model):
    """

    user_id
    buy_date
    notes
    sku
    payment_type
    total_price
    quantity
    seller_id
    """
    minimum_price = 10.5
    maximum_price = 1000

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    buy_date = models.DateTimeField(default=datetime.datetime.utcnow())
    notes = models.TextField(default='')
    sku = models.CharField(max_length=52, blank=False, null=False, default='')
    total_price = models.FloatField(blank=False, null=False, default=0.0)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    seller_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='seller', null=True)

    def __str__(self):
        return f'Orden {self.pk} de {self.user.first_name} compró {self.sku}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.total_price < self.minimum_price:
            logger.debug(f'Ajustando precio mínimo a {self.minimum_price}')
            self.total_price = self.minimum_price

        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Company(models.Model):
    """
    name
    contact_phone
    support_phone
    sales_phone

    """
    name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=18)
    support_phone = models.CharField(max_length=18)
    sales_phone = models.CharField(max_length=18)


class Client(models.Model):
    """
    client_no
    name

    """
    client_no = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'Cliente: {self.pk} - {self.name}'
