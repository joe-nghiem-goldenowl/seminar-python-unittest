from django.db import models

class Car(models.Model):
    price = models.FloatField(null=False)
    fuel_type = models.CharField(null=False, max_length=100)
    name = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'id': self.id,
            'price': self.price,
            'name': self.name,
            'fuel_type': self.fuel_type,
        }
