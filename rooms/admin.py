from django.contrib import admin
from . import models
from django.utils.html import mark_safe

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by",)    

    def used_by(self, obj):
        return obj.rooms.count()
    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""
    
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "describtion", "country", "city", "address", "price")},
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

    list_display = ("name", "country", "city", "price", "guests", "beds", "bedrooms", "baths", "check_in", "check_out", "instant_book", "count_amenities", "count_photos", "total_rating",)

    ordering = ("price",)

    list_filter = ("instant_book", "host__superhost", "room_type", "amenity", "facility", "house_rules", "city", "country")

    search_fields = ("^city", "^host__username")

    raw_id_fields = ("host",)

    filter_horizontal = ("amenity", "facility", "house_rules",)

    def count_amenities(self, obj):
        return obj.amenity.count()

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100px" src = "{obj.file.url}" />')
    get_thumbnail.short_description = "Thumnail"
