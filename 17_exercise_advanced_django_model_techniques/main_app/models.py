from decimal import Decimal
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


from main_app.validators import PhoneNumberValidator, ValidateCustomerName
from main_app.mixin import RechargeEnergyMixin

class Customer(models.Model):
    name = models.CharField(
        max_length=100, 
        validators=[ValidateCustomerName(message="Name can only contain letters and spaces")
        ]
    )

    age = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(18, message="Age must be greater than or equal to 18")
        ]
    )

    email = models.EmailField(
        error_messages={
            'invalid': "Enter a valid email address."
        })

    phone_number = models.CharField(
        max_length=13,
        validators=[
            PhoneNumberValidator(
                message="Phone number must start with '+359' followed by 9 digits"
            )]
    )

    website_url = models.URLField(error_messages={
        'invalid': "Enter a valid URL"
   } )


class BaseMedia(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, message= "Author must be at least 5 characters long")

        ]
    )

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(6, message="ISBN must be at least 6 characters long")
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, message="Director must be at least 8 characters long")
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"

class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, message="Artist must be at least 9 characters long")
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"



class Product(models.Model):
    TAX_RATES = Decimal('0.08')
    SHIPPING_COST = Decimal('2.00')
    TYPE_PRODUCT = 'Product'

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        return self.price * self.TAX_RATES

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * self.SHIPPING_COST

    def format_product_name(self):
        return f"{self.TYPE_PRODUCT}: {self.name}"

class DiscountedProduct(Product):
    TAX_RATES = Decimal('0.05')
    SHIPPING_COST = Decimal('1.50')
    ORIGINAL_PRICE = Decimal('20')
    TYPE_PRODUCT = 'Discounted Product'


    def calculate_price_without_discount(self):
        return Decimal(str(self.price)) * (1 + self.ORIGINAL_PRICE)

    class Meta:
        proxy = True


class Hero(models.Model, RechargeEnergyMixin):
    ENERGY_DECREASES = 0

    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField()

    @property
    def energy_max_message(self):
        return ''

    @property
    def energy_min_message(self):
        return ''

    def hellp_def(self):
        if self.energy < self.ENERGY_DECREASES:
            return self.energy_max_message

        self.energy = max(self.energy - self.ENERGY_DECREASES, 1)

        return self.energy_min_message

class SpiderHero(Hero):
    ENERGY_DECREASES = 80

    def swing_from_buildings(self):
        return self.hellp_def()

    @property
    def energy_max_message(self):
        return f"{self.name} as Spider Hero is out of web shooter fluid"

    @property
    def energy_min_message(self):
        return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:
        proxy = True

class FlashHero(Hero):
    ENERGY_DECREASES = 65

    def run_at_super_speed(self):
        return self.hellp_def()

    @property
    def energy_max_message(self):
        return f"{self.name} as Flash Hero needs to recharge the speed force"

    @property
    def energy_min_message(self):
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:
        proxy = True