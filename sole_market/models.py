from django.db import models
from django.utils.translation import gettext_lazy as gtl


from sole_store.settings import CORS_ALLOWED_ORIGINS as origins

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


