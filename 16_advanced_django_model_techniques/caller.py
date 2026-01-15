import os
import django
from django.core.exceptions import ValidationError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Restaurant, Menu, RestaurantReview

restaurant1 = Restaurant.objects.filter(name="Restaurant A", location="123 Main St.", description="A cozy restaurant", rating=4.88).first()
restaurant2 = Restaurant.objects.filter(name="Restaurant B", location="456 Elm St.",  description="Charming restaurant", rating=3.59)

RestaurantReview.objects.filter(reviewer_name="Bob", restaurant=restaurant1, review_content="Good experience overall.", rating=4)
RestaurantReview.objects.filter(reviewer_name="Aleks", restaurant=restaurant1, review_content="Great food and service!", rating=5)
RestaurantReview.objects.filter(reviewer_name="Charlie", restaurant=restaurant2, review_content="It was ok!", rating=2)

duplicate_review = RestaurantReview(reviewer_name="Aleks", restaurant=restaurant1, review_content="Another great meal!", rating=5)

try:
    duplicate_review.full_clean()
    duplicate_review.save()
except ValidationError as e:
    print(f"Validation Error: {e}")


print("All Restaurant Reviews:")
for review in RestaurantReview.objects.all():
    print(f"Reviewer: {review.reviewer_name}, Rating: {review.rating}, Restaurant: {review.restaurant.name}")