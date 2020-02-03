from django.db import models
from django.shortcuts import reverse
from tinymce.models import HTMLField
from user.models import Profile

LABEL_CHOICES = (
    ('PR', 'prefered'),
    ('MO', 'most viewed'),
    ('SA', 'sale')
)
LABEL_BG_CHOICES = (
    ('PR', 'primary'),
    ('SE', 'secondary'),
    ('DA', 'danger'),
    ('IN', 'info')
)
CATEGORY_CHOICES = (
    ('TS', 'Shirt'),
    ('PA', 'Pants'),
    ('UN', 'Underware'),
    ('SH', 'Shoe')
)


class Product(models.Model):
    seller = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=5000)
    specification = HTMLField('Specification', blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='store/')
    timestamp = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=2,
                             choices=LABEL_CHOICES, blank=True)
    label_bg = models.CharField(max_length=2,
                                choices=LABEL_BG_CHOICES, blank=True)
    category = models.CharField(max_length=2,
                                choices=CATEGORY_CHOICES, blank=True)
    sold = models.PositiveIntegerField(default='0', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={'slug': self.slug})

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)


class OrderProduct(models.Model):
    user = models.ForeignKey(Profile,
                             on_delete=models.CASCADE)
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.profile


class Cart(models.Model):
    user = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name='product')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name
