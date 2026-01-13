from django.core.exceptions import ValidationError

def validate_menu_categories(value):
    category = ["Appetizers", "Main Course", "Desserts"]

    for item in category:
        if item.lower() not in value.lower():
            raise ValidationError ('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')