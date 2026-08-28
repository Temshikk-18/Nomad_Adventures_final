from asgiref.sync import sync_to_async
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods

from .forms import BookingForm
from .models import Booking, Category, Region, Tour


async def _all(queryset, language="ru"):
    items = [obj async for obj in queryset]
    for obj in items:
        obj._lang = language
    return items


async def home(request):
    language = request.LANGUAGE_CODE[:2]
    regions = await _all(Region.objects.filter(is_featured=True).prefetch_related("images", "places")[:7], language)
    for region in regions:
        region.place_count = sum(1 for p in region.places.all() if p.is_active)
    categories = await _all(Category.objects.filter(is_active=True).prefetch_related("tours"), language)
    for category in categories:
        active = [t for t in category.tours.all() if t.is_active]
        category.active_tour_count = len(active)
        days = [t.days for t in active]
        category.min_days = min(days) if days else 0
        category.max_days = max(days) if days else 0
    tours = await _all(Tour.objects.filter(is_active=True, is_featured=True).select_related("region", "category")[:6], language)
    return TemplateResponse(request, "home.html", {"regions": regions, "categories": categories, "tours": tours})


async def regions(request):
    language = request.LANGUAGE_CODE[:2]
    items = await _all(Region.objects.all().prefetch_related("images", "places"), language)
    for region in items:
        region.place_count = sum(1 for p in region.places.all() if p.is_active)
    return TemplateResponse(request, "regions.html", {"regions": items})


async def region_detail(request, slug):
    language = request.LANGUAGE_CODE[:2]
    region = await Region.objects.prefetch_related("images", "places__images", "tours__category").aget(slug=slug)
    region._lang = language
    region.place_count = sum(1 for p in region.places.all() if p.is_active)
    for place in region.places.all():
        place.region._lang = language
    tours = await _all(Tour.objects.filter(region=region, is_active=True).select_related("category"), language)
    return TemplateResponse(request, "region_detail.html", {"region": region, "tours": tours})


async def tour_list(request):
    qs = Tour.objects.filter(is_active=True).select_related("region", "category")
    category = request.GET.get("category")
    if category:
        qs = qs.filter(category__slug=category)
    language = request.LANGUAGE_CODE[:2]
    tours = await _all(qs, language)
    categories = await _all(Category.objects.filter(is_active=True).prefetch_related("tours"), language)
    for cat in categories:
        active = [t for t in cat.tours.all() if t.is_active]
        cat.active_tour_count = len(active)
        days = [t.days for t in active]
        cat.min_days = min(days) if days else 0
        cat.max_days = max(days) if days else 0
    return TemplateResponse(request, "tours.html", {"tours": tours, "categories": categories, "category": category})


async def tour_detail(request, slug):
    language = request.LANGUAGE_CODE[:2]
    tour = await Tour.objects.select_related("region", "category").prefetch_related("itinerary").aget(slug=slug)
    tour._lang = language
    tour.region._lang = language
    tour.category._lang = language
    for day in tour.itinerary.all():
        day._lang = language
    return TemplateResponse(request, "tour_detail.html", {"tour": tour, "form": BookingForm()})


@require_http_methods(["GET", "POST"])
async def book_tour(request, slug):
    language = request.LANGUAGE_CODE[:2]
    tour = await Tour.objects.select_related("region", "category").aget(slug=slug)
    tour._lang = language
    tour.region._lang = language
    tour.category._lang = language
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            await sync_to_async(booking.save)()
            return TemplateResponse(request, "booking_success.html", {"booking": booking})
    else:
        form = BookingForm()
    return TemplateResponse(request, "tour_detail.html", {"tour": tour, "form": form})


async def booking_success(request):
    return TemplateResponse(request, "booking_success.html", {})
