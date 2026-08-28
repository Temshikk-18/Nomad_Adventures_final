Django i18n is enabled for interface text. Add translations with:
python manage.py makemessages -l ky -l ru -l en
python manage.py compilemessages
Database tourism content is stored in three fields (_ky, _ru, _en), so the site does not require django-modeltranslation.
