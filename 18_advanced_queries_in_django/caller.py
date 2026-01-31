import os
from functools import total_ordering

import django
from django.db.models import Count, Sum

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


def product_quantity_ordered():
    products = (OrderProduct.objects.values('product__name')
    .annotate(total_quantity=Sum('quantity'))
    .filter(total_quantity__gt=0)
    .order_by("-total_quantity", "product__name")
    )

    result = []
    for product in products:

        result.append(f"Quantity ordered of {product['product__name']}: {product['total_quantity']}")
    return '\n'.join(result)

def ordered_products_per_customer():
    orders = (Order.objects.prefetch_related('orderproduct_set__product__category')
              .filter(orderproduct__isnull=False)).distinct().order_by('id')

    result = []
    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")

        order_products = order.orderproduct_set.all()

        for order_product in order_products:
            product = order_product.product
            category = product.category.name

            result.append(f"- Product: {product.name}, Category: {category}")
    return '\n'.join(result)

def filter_products():
    products_price = Product.objects.filter(is_available=True, price__gt=3.00).order_by(
        "-price", 'name')
    result = []
    for product in products_price:
        result.append(f"{product.name}: {product.price}lv.")
    return '\n'.join(result)

# print(product_quantity_ordered())
# print(ordered_products_per_customer())
print(filter_products())

