import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# def validate_customer_name(value):
#     for name in value:
#         if not(name.isalpha() or name.isspace()):
#             raise ValidationError("Name can only contain letters and spaces")

@deconstructible
class ValidateCustomerName:

    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        for char in value:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError(message=self.message)


@deconstructible
class PhoneNumberValidator:

    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        if not re.match('^\+359\{9}$', value):
            raise ValidationError(message=self.message)


# @deconstructible
# class BookAuthorName:
#     def __init__(self, message):
#         self.message = message
#
#     def __call__(self, value):
#         if len(value) < 5:
#             raise ValidationError(message=self.message)