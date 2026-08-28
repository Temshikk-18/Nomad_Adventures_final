from django.core.management.base import BaseCommand
from tours.models import Category, Place, Region, Tour, TourDay

class Command(BaseCommand):
    help = "Create demo categories, seven oblasts, beautiful places and tours."
    def handle(self, *args, **kwargs):
        categories = [
            ("mountains","Тоолор турлары","Горные туры","Mountain tours","Эң кооз тоолорго жөө жүрүү, альпинизм жана трекинг.","Походы, треккинг и альпинизм в самых красивых горах.","Hiking, trekking and climbing in the most beautiful mountains.","🏔️"),
            ("lakes","Көлдөр","Озёра","Lakes","Ысык-Көл жана башка кооз көлдөргө турлар.","Туры к Иссык-Кулю и другим красивым озёрам.","Trips to Issyk-Kul and other beautiful lakes.","🌊"),
            ("culture","Маданий турлар","Культурные туры","Cultural tours","Тарыхый жайлар, музейлер жана маданият.","Исторические места, музеи и культура.","Historic places, museums and local culture.","🏺"),
            ("adventure","Приключения","Приключения","Adventure","Ат минүү, рафтинг, джип жана активдүү турлар.","Конные прогулки, рафтинг, джип-туры и активный отдых.","Horse riding, rafting, jeep tours and active travel.","🐎"),
            ("nomad","Көчмөндөр турлары","Туры кочевников","Nomad tours","Көчмөн жашоосу, боз үй жана салттуу тамактар.","Кочевой быт, юрты и традиционная кухня.","Nomadic life, yurts and traditional food.","⛺"),
            ("winter","Кышкы турлар","Зимние туры","Winter tours","Ала-Тоо, лыжа, сноуборд жана карлуу эс алуу.","Ала-Тоо, лыжи, сноуборд и снежный отдых.","Ala-Too, skiing, snowboarding and snowy escapes.","❄️"),
        ]
        cat_map = {}
        for i, row in enumerate(categories):
            slug,nky,nru,nen,dky,dru,den,icon=row
            cat,_=Category.objects.update_or_create(slug=slug,defaults=dict(name_ky=nky,name_ru=nru,name_en=nen,description_ky=dky,description_ru=dru,description_en=den,icon=icon,sort_order=i))
            cat_map[slug]=cat

        regions = [
            ("chuy","Чүй облусу","Чуйская область","Chuy Region","Борборго жакын тарых, капчыгайлар жана тоолуу жаратылыш.","История, ущелья и горная природа рядом со столицей.","History, gorges and mountain nature near the capital."),
            ("issyk-kul","Ысык-Көл облусу","Иссык-Кульская область","Issyk-Kul Region","Көк көл, кызыл капчыгайлар жана бийик тоолор.","Синее озеро, красные каньоны и высокие горы.","Blue lake, red canyons and high mountains."),
            ("naryn","Нарын облусу","Нарынская область","Naryn Region","Кең жайлоолор, Сон-Көл жана көчмөндөрдүн дүйнөсү.","Широкие пастбища, Сон-Куль и мир кочевников.","Wide pastures, Song-Kul and the nomadic world."),
            ("osh","Ош облусу","Ошская область","Osh Region","Байыркы шаарлар, Сулайман-Тоо жана түштүктүн өзгөчө маданияты.","Древние города, Сулейман-Тоо и культура юга.","Ancient cities, Sulaiman-Too and southern culture."),
            ("jalal-abad","Жалал-Абад облусу","Джалал-Абадская область","Jalal-Abad Region","Арсланбап, Сары-Челек жана жашыл токойлор.","Арсланбоб, Сары-Челек и зелёные леса.","Arslanbob, Sary-Chelek and lush forests."),
            ("talas","Талас облусу","Таласская область","Talas Region","Манас өрөөнү, тарых жана тоо этектери.","Долина Манаса, история и предгорья.","Manas valley, history and foothills."),
            ("batken","Баткен облусу","Баткенская область","Batken Region","Өрүк бактары, капчыгайлар жана уникалдуу тоо ландшафттары.","Абрикосовые сады, ущелья и уникальные горные ландшафты.","Apricot orchards, gorges and unique mountain landscapes."),
        ]
        region_map={}
        for slug,nky,nru,nen,dky,dru,den in regions:
            r,_=Region.objects.update_or_create(slug=slug,defaults=dict(name_ky=nky,name_ru=nru,name_en=nen,short_description_ky=dky,short_description_ru=dru,short_description_en=den,cover_url=urls.get(slug,""),is_featured=True))
            region_map[slug]=r

        places = {
            "chuy":[("ala-archa","Ала-Арча","Ала-Арча","Ala-Archa","Бишкекке жакын эң белгилүү улуттук парк.","Известный национальный парк рядом с Бишкеком.","The famous national park near Bishkek."),("burana","Бурана мунарасы","Башня Бурана","Burana Tower","Улуу Жибек жолунун тарыхый эстелиги.","Исторический памятник Великого шёлкового пути.","A historic monument of the Silk Road.")],
            "issyk-kul":[("issyk-kul","Ысык-Көл","Иссык-Куль","Issyk-Kul","Кыргызстандын бермети.","Жемчужина Кыргызстана.","The pearl of Kyrgyzstan."),("skazka","Сказка каньону","Каньон Сказка","Skazka Canyon","Кызыл аскалар жана фантастикалык формалар.","Красные скалы и фантастические формы.","Red rocks and fantastical shapes.")],
            "naryn":[("song-kul","Соң-Көл","Сон-Куль","Song-Kul","Бийик тоодогу көгүлтүр көл жана жайлоо.","Высокогорное озеро и летние пастбища.","High-altitude lake and summer pastures."),("tash-rabat","Таш-Рабат","Таш-Рабат","Tash-Rabat","Тоолордогу байыркы кербен сарай.","Древний караван-сарай в горах.","An ancient caravanserai in the mountains.")],
            "osh":[("sulaiman-too","Сулайман-Тоо","Сулейман-Тоо","Sulaiman-Too","Ош шаарынын жүрөгүндөгү ыйык тоо.","Священная гора в сердце Оша.","The sacred mountain in the heart of Osh."),("uzgen","Өзгөн мунаралары","Узгенские минареты","Uzgen Minarets","Орто кылымдагы тарыхый комплекс.","Средневековый исторический комплекс.","A medieval historical complex.")],
            "jalal-abad":[("arslanbob","Арсланбап","Арсланбоб","Arslanbob","Жаңгак токойлору жана шаркыратмалар.","Ореховые леса и водопады.","Walnut forests and waterfalls."),("sary-chelek","Сары-Челек","Сары-Челек","Sary-Chelek","Тоолордун арасындагы тунук көлдөрдүн аймагы.","Край чистых озёр среди гор.","A region of clear mountain lakes.")],
            "talas":[("manas-ordo","Манас Ордо","Манас Ордо","Manas Ordo","Манас эпосунун маданий жайы.","Культурный комплекс эпоса Манаса.","Cultural complex dedicated to the Manas epic.")],
            "batken":[("aigul","Айгүл-Тоо","Айгуль-Тоо","Aigul-Too","Жазында сейрек Айгүл гүлү менен белгилүү тоо.","Гора, известная редким цветком Айгуль.","A mountain known for the rare Aigul flower.")],
        }
        for rslug, items in places.items():
            r=region_map[rslug]
            for idx,(slug,nky,nru,nen,dky,dru,den) in enumerate(items):
                demo_url = {"chuy":"https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1000&q=80","issyk-kul":"https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1000&q=80","naryn":"https://images.unsplash.com/photo-1511497584788-876760111969?auto=format&fit=crop&w=1000&q=80","osh":"https://images.unsplash.com/photo-1530789253388-582c481c54b0?auto=format&fit=crop&w=1000&q=80","jalal-abad":"https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1000&q=80","talas":"https://images.unsplash.com/photo-1482192505345-5655af888cc4?auto=format&fit=crop&w=1000&q=80","batken":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1000&q=80"}.get(rslug, "")
                Place.objects.update_or_create(slug=slug,defaults=dict(region=r,name_ky=nky,name_ru=nru,name_en=nen,description_ky=dky,description_ru=dru,description_en=den,image_url=demo_url,sort_order=idx,is_active=True))

        tours=[
            ("ala-archa-day","Ала-Арча — бир күндүк трекинг","Ала-Арча — однодневный трекинг","Ala-Archa — day trek","chuy","mountains",1,95),("issyk-kul-week","Ысык-Көл жана каньондор","Иссык-Куль и каньоны","Issyk-Kul & canyons","issyk-kul","lakes",4,390),("song-kul-nomad","Соң-Көлдөгү көчмөн жашоо","Кочевая жизнь на Сон-Куле","Nomad life at Song-Kul","naryn","nomad",3,330),("osh-culture","Ош жана Сулайман-Тоо","Ош и Сулейман-Тоо","Osh & Sulaiman-Too","osh","culture",2,180),("arslanbob-adventure","Арсланбап укмуштуу саякаты","Приключение в Арсланбобе","Arslanbob adventure","jalal-abad","adventure",5,450),("winter-ala-archa","Кышкы Ала-Арча","Зимняя Ала-Арча","Winter Ala-Archa","chuy","winter",2,220)]
        for slug,tky,tru,ten,rslug,cslug,days,price in tours:
            r=region_map[rslug]; c=cat_map[cslug]
            Tour.objects.update_or_create(slug=slug,defaults=dict(title_ky=tky,title_ru=tru,title_en=ten,description_ky=f"{tky}. Кыргызстанды жакындан тааныңыз.",description_ru=f"{tru}. Откройте Кыргызстан ближе.",description_en=f"{ten}. Experience Kyrgyzstan up close.",region=r,category=c,days=days,price_usd=price,is_active=True,is_featured=True))
        self.stdout.write(self.style.SUCCESS("Demo categories, 7 regions, places and tours created."))
