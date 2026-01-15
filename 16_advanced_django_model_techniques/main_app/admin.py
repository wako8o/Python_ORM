from django.contrib import admin

from main_app.models import Restaurant, RestaurantReview

# Register your models here.

admin.site.register(Restaurant)


@admin.register(RestaurantReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'restaurant', 'rating')
    search_fields = ('reviewer_name', 'restaurant__name', 'rating')
