from django.db import models
from user.models import CustomUser
from products.models import Product

class UserProductInterest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)  # for personalization

    def __str__(self):
        return f"{self.user.username} ↔ {self.product.name}"