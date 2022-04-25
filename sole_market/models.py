from io import BytesIO
from django.db import models
from django.utils.translation import gettext_lazy as gtl
from django.core.files import File
from PIL import Image

from django.conf import settings

origins = settings.CORS_ALLOWED_ORIGINS[0]

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        help_text=gtl("Name of category"),
    )
    slug = models.SlugField(
        blank=False,
        null=False,
        unique=True,
        help_text=gtl(
            "slug for category. Used for URL, can not contain spaces"
        ),
    )

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        help_text=gtl("Name of product"),
    )
    slug = models.SlugField(
        blank=False,
        null=False,
        unique=True,
        help_text=gtl(
            "slug for product. Used for URL, can not contain spaces"
        ),
    )
    description = models.TextField(blank=True, null=True, unique=False)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=False, null=False
    )
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_image(self):
        if self.image:
            return f"{origins}/{self.image.url}"

    def get_thumbnail(self):
        if self.thumbnail:
            return f"{origins}/{self.thumbnail.url}"
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return f"{origins}/{self.thumbnail.url}"
            else:
                return ""

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumbs_io = BytesIO()
        img.save(thumbs_io, "JPEG", quality=85)
        thumbnail = File(thumbs_io, name=image.name)
        return thumbnail
