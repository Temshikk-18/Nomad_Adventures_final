from django.contrib import admin
from .models import Booking, Category, Place, PlaceImage, Region, RegionImage, Tour, TourDay


class RegionImageInline(admin.TabularInline):
    model = RegionImage
    extra = 3
    fields = ("image", "caption_ky", "caption_ru", "caption_en", "sort_order")


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 3
    fields = ("image", "caption_ky", "caption_ru", "caption_en", "sort_order")


class TourDayInline(admin.TabularInline):
    model = TourDay
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "slug", "sort_order", "is_active")
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("name_ru",)}
    ordering = ("sort_order", "name_ru")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "is_featured")
    list_filter = ("is_featured",)
    prepopulated_fields = {"slug": ("name_ru",)}
    inlines = [RegionImageInline]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "region", "is_active", "sort_order")
    list_filter = ("region", "is_active")
    prepopulated_fields = {"slug": ("name_ru",)}
    inlines = [PlaceImageInline]


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "category", "region", "days", "price_usd", "is_active")
    list_filter = ("category", "region", "is_active", "is_featured")
    prepopulated_fields = {"slug": ("title_ru",)}
    inlines = [TourDayInline]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "tour", "travel_date", "people", "created_at")
    list_filter = ("travel_date", "created_at")
    search_fields = ("name", "email", "phone")