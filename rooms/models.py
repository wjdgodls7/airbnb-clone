from django.db import models
from core import models as core_models
from django_countries.fields import CountryField


class AbstractItem(core_models.TimeStampModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name_plural = "Room Types"


class Amenity(AbstractItem):
    
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amentities"


class Facility(AbstractItem):
    
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    
    """HouseRule Model Definition"""

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampModel):

    """Room Model Definition"""
    
    name = models.CharField(max_length=140)
    describtion = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # foreignkey는 한 모델을 다른 모델과 연결시켜주는 역활을 함
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField("Amenity", blank=True)
    facility = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name