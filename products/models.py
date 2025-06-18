from django.db import models
import uuid

# DRY BaseModel with UUID and timestamps
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Avoids creating a separate table

# Product model
class Product(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    demo_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

# Metadata for each product (like weight, quantity, restrictions)
class ProductMetaInformation(BaseModel):
    MEASUREMENT_UNITS = (
        ("KG", "Kilogram"),
        ("L", "Litre"),
        ("PCS", "Pieces"),
        ("ML", "Millilitre"),
        ("None", "None")
    )

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta_info")
    measurement_unit = models.CharField(max_length=10, choices=MEASUREMENT_UNITS, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    is_restricted = models.BooleanField(default=False)
    restrict_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Meta for {self.product.name}"

# Product images (Multiple images per product)
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"
