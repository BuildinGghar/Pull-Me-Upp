from django.db import models

class Service(models.Model):
    WOMEN = 'W'
    MEN = 'M'
    KIDS = 'K'

    SERVICE_TYPE_CHOICES = [
        (WOMEN, 'Women Price'),
        (MEN, 'Men Price'),
        (KIDS, 'Kids Price'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    service_type = models.CharField(max_length=1, choices=SERVICE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} - ₹{self.price} ({self.get_service_type_display()})"
