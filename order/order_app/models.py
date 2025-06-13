from django.db import models
import uuid


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    product_id = models.PositiveIntegerField()
    
