from encodings import search_function
from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""
    
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "describtion", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "More About the Space",
            {"fields": ("amenity", "facility", "house_rules")},
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = ("name", "country", "city", "price", "guests", "beds", "bedrooms", "baths", "check_in", "check_out", "instant_book", "count_amenities",)

    ordering = ("price",)

    list_filter = ("instant_book", "host__superhost", "room_type", "amenity", "facility", "house_rules", "city", "country")

    search_fields = ("^city", "^host__username")

    filter_horizontal = ("amenity", "facility", "house_rules",)

    def count_amenities(self, obj):
        return self



@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass


