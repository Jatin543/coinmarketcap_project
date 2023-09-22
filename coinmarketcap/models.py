from django.db import models

# Create your models here.

class CoinData(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    one_hour_change = models.CharField(max_length=255)
    twenty_four_hour_change = models.CharField(max_length=255)
    seven_day_change = models.CharField(max_length=255)
    market_cap = models.CharField(max_length=255)
    volume_24h = models.CharField(max_length=255)
    circulating_supply = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']