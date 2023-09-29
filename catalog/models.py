from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse


class ClothingType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} ({self.description})"


class Clothing(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    clothing_type = models.ForeignKey(ClothingType, on_delete=models.CASCADE, related_name="clothes")
    materials = models.ManyToManyField(Material, related_name="clothes")
    size = models.ManyToManyField(Size, related_name="clothes")
    designer = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="clothes")
    image = models.ImageField(upload_to="static/images/clothing", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} by {self.designer} - ${self.price}"

    def get_absolute_url(self):
        return reverse("catalog:clothing-detail", args=[str(self.id)])


class Designer(AbstractUser):
    pseudonym = models.CharField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        ordering = ['username']
        verbose_name = "designer"
        verbose_name_plural = "designers"

    def __str__(self) -> str:
        return f"{self.username} {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("catalog:designer-detail", args=[str(self.id)])
