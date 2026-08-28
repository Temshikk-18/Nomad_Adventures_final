from django.db import models


class Category(models.Model):
    slug = models.SlugField(unique=True)
    name_ky = models.CharField(max_length=120)
    name_ru = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120)
    description_ky = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    icon = models.CharField(max_length=20, default="🏔️")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "name_ru"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name_ru

    def localized(self, field):
        lang = getattr(self, "_lang", "ru")[:2]
        return getattr(self, f"{field}_{lang}", getattr(self, f"{field}_ru"))



class Region(models.Model):
    slug = models.SlugField(unique=True)
    name_ky = models.CharField(max_length=120)
    name_ru = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120)
    short_description_ky = models.TextField(blank=True)
    short_description_ru = models.TextField(blank=True)
    short_description_en = models.TextField(blank=True)
    image = models.ImageField(upload_to="regions/covers/", blank=True)
    cover_url = models.URLField(blank=True, help_text="Демо-сүрөт үчүн URL. Upload image болсо, ал артыкчылыктуу колдонулат.")
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ["name_ru"]
        verbose_name = "Область"
        verbose_name_plural = "Области"

    def __str__(self):
        return self.name_ru

    def localized(self, field):
        lang = getattr(self, "_lang", "ru")[:2]
        return getattr(self, f"{field}_{lang}", getattr(self, f"{field}_ru"))

    @property
    def gallery_images(self):
        return self.images.all()



class RegionImage(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="regions/gallery/")
    caption_ky = models.CharField(max_length=180, blank=True)
    caption_ru = models.CharField(max_length=180, blank=True)
    caption_en = models.CharField(max_length=180, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Фото области"
        verbose_name_plural = "Фото области"

    def __str__(self):
        return f"{self.region.name_ru} #{self.pk}"

    def localized(self, field):
        lang = getattr(self.region, "_lang", "ru")[:2]
        return getattr(self, f"{field}_{lang}", getattr(self, f"{field}_ru"))


class Place(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="places")
    slug = models.SlugField(unique=True)
    name_ky = models.CharField(max_length=160)
    name_ru = models.CharField(max_length=160)
    name_en = models.CharField(max_length=160)
    description_ky = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    image_url = models.URLField(blank=True, help_text="Демо-сүрөт URL")
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name_ru"]
        verbose_name = "Красивое место"
        verbose_name_plural = "Красивые места"

    def __str__(self):
        return f"{self.name_ru} — {self.region.name_ru}"

    def localized(self, field):
        lang = getattr(self.region, "_lang", "ru")[:2]
        return getattr(self, f"{field}_{lang}", getattr(self, f"{field}_ru"))


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="places/")
    caption_ky = models.CharField(max_length=180, blank=True)
    caption_ru = models.CharField(max_length=180, blank=True)
    caption_en = models.CharField(max_length=180, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Фото места"
        verbose_name_plural = "Фото места"

    def localized(self, field):
        lang = getattr(self.place.region, "_lang", "ru")[:2]
        return getattr(self, f"{field}_{lang}", getattr(self, f"{field}_ru"))


class Tour(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="tours")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="tours")
    slug = models.SlugField(unique=True)
    title_ky = models.CharField(max_length=180)
    title_ru = models.CharField(max_length=180)
    title_en = models.CharField(max_length=180)
    description_ky = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    days = models.PositiveIntegerField(default=1)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="tours/", blank=True)
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

    def __str__(self):
        return self.title_ru

    def localized(self, field):
        lang = getattr(self, "_lang", "ru")[:2]
        return getattr(self, f"{field}_{lang}", getattr(self, f"{field}_ru"))


class TourDay(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="itinerary")
    day_number = models.PositiveIntegerField()
    title_ky = models.CharField(max_length=180)
    title_ru = models.CharField(max_length=180)
    title_en = models.CharField(max_length=180)
    description_ky = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    class Meta:
        ordering = ["day_number"]
        unique_together = ("tour", "day_number")
        verbose_name = "День тура"
        verbose_name_plural = "Дни тура"

    def localized(self, field):
        lang = getattr(self.tour, "_lang", "ru")[:2]
        return getattr(self, f"{field}_{lang}", getattr(self, f"{field}_ru"))


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    people = models.PositiveIntegerField(default=1)
    travel_date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.tour}"
