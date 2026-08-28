# Nomad Adventures — Kyrgyzstan

Django 6 + Django Templates tourism website for Kyrgyzstan.

## Main features
- KY / RU / EN language switcher with Django LocaleMiddleware.
- Modern homepage: hero, 6 tour categories, duration range and number of tours.
- Exactly 7 oblasts on the homepage.
- Each oblast has a detail page with a photo gallery and beautiful places.
- `RegionImageInline`: add many region photos directly while editing a Region in Django Admin.
- `PlaceImageInline`: add many photos for each beautiful place.
- Tours belong to a category and oblast; duration is shown everywhere.
- Async Django views with `async def` and `sync_to_async` for the booking write.
- WhatsApp, phone and Instagram buttons.
- Responsive/mobile navigation and touch-friendly horizontal category filters.

## Admin workflow
1. `python manage.py migrate`
2. `python manage.py createsuperuser`
3. `python manage.py runserver`
4. Open `/admin/`.
5. Create/edit a **Category** and add tours to it.
6. Create/edit an **Область**. Inside the same page, the **Фото области** inline lets you upload many images.
7. Create **Красивое место**, select its oblast, then use **Фото места** inline to upload multiple images.

## Demo content
Run:

```bash
python manage.py seed_demo
```

This creates 6 categories, 7 oblasts, demo beautiful places and demo tours. Demo image URLs are used as fallbacks so the site is visually populated before you upload your own photos.

## Run

```bash
python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```
