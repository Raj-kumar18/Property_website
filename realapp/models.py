from django.db import models
from autoslug import AutoSlugField
# Create your models here.

TYPE_CHOICES = [
    ('Sale','Sale'),
    ('Rent','Rent')
    ]

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField(null=True,blank=True)
    bathrooms = models.DecimalField(max_digits=4, decimal_places=2,null=True,blank=True)
    sqft = models.IntegerField()
    photo = models.ImageField(upload_to='property_photos')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',null=True,default=None)
    types = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title
