from django.db import models           
from django.utils.translation import gettext_lazy as _
import uuid


from django.core.mail import send_mail

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from accounts.models import User



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.parent:
            return f'{self.name} -> {self.parent.name}'
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Product')
    description = models.TextField()
    price = models.PositiveIntegerField(null=True)
    quntity = models.PositiveSmallIntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_sum = models.PositiveIntegerField()
    deliver_type = models.CharField(max_length=200)
    delivered = models.CharField(max_length=100)
    creadet_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    extra_info = models.TextField()


class Order_product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantiny = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()