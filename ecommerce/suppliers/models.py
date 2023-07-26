from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from ecommerce.catalogue.models import Product


class Supplier(models.Model):
    BUSINESS_SCALE = [
        ("BB", "Big business")
        ("SB", "Small business")
        ("p", "Person")
    ]
    date_created = models.DateTimeField(_("Date created"),
                                        auto_now_add=True)

    date_updated = models.DateTimeField(_("Date Updated",
                                          auto_now=True))

    date_deleted = models.DateTimeField(_("Date Deleted"),
                                        null=True)

    scale_of_supplier = models.CharField(_("scale of business"),
                                         max_length=2, choices=BUSINESS_SCALE)

    brand_name = models.CharField(_("Brand name"), max_length=100)

    about_supplier = models.TextField(_("A summery about supplier"),
                                      blank=True)

    email = models.EmailField(_("Email to contact with supplier"))

    phone_number = models.CharField(_("Phone nuber to contact with supplier"), max_length=15)


