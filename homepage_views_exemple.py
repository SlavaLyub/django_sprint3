from django.shortcuts import render
from ice_cream.models import IceCream, Category
# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q


def index(request):
    template = 'homepage/index.html'

    # запрашиваем конкретные значения из объекта БД и применяем фильтр с модификатором
    # ice_cream_list = IceCream.objects.values('id', 'title', 'description').filter(is_on_main=True)

    # новый запрос Исключи те объекты, у которых is_published=False:
    # ice_cream_list = IceCream.objects.values('id', 'title', 'description').exclude(is_published=False)

    # Два в одном! Объекты, которые соответствуют сразу двум условиям, запись через запятую
    # ice_cream_list = IceCream.objects.values('id', 'title', 'description').filter(is_published=True, is_on_main=True)

    # Делаем запрос, объединяя два условия через Q-объекты и оператор AND(&)(есть 3 варианта написания, все в теории 6-го спринта):
    # ice_cream_list = IceCream.objects.values('id', 'title', 'description').filter(Q(is_published=True) & Q(is_on_main=True))

    # получаем записи, у которых поле is_on_main ИЛИ поле is_published равно True запись через Q объект, в теории пример без Q объектов
    # ice_cream_list = IceCream.objects.values('id').filter(Q(is_published=True) | Q(is_on_main=True))

    # получаем записи, у которых поле is_published равно True и одновременно поле is_on_main не равно False (НЕ НЕ равно True) ~знак не равно :
    # ice_cream_list = IceCream.objects.values('id').filter(Q(is_published=True) & ~Q(is_on_main=False))

    # Делаем запрос из задания
    # ice_cream_list = IceCream.objects.values('title', 'description').filter(Q(is_published=True)& Q(is_on_main=True) | Q(title__contains='пломбир'))
    # ice_cream_list = IceCream.objects.values('title', 'description').filter(Q(is_on_main=True)& Q(is_published=True)| Q(title__contains='пломбир')& Q(is_published=True))
    # пример запроса со скобками, джанго автоматом проставит скобки на основе приоритетов логических операций
    # используется Модификатор сравнения __contains
    # ice_cream_list = IceCream.objects.values('title', 'description').filter((Q(is_on_main=True) & Q(is_published=True))| (Q(title__contains='пломбир') & Q(is_published=True))) 

    # Ограничим число возвращаемых объектов до трёх: с помощью среза
    # ice_cream_list = IceCream.objects.values('id', 'title', 'description').filter(is_published=True, is_on_main=True).order_by('title')[0:3]

    # обращения к связанным объектам
    # запрос атрибута объекта, ссылающийся на другую модель
    # и прямо в HTML-шаблоне получить значения полей связанного объекта
    # через точечную нотацию.
    # запрос №2
    # ice_cream_list = IceCream.objects.all()
    
    # Метод .values() может вернуть не только поля запрошенной модели,
    # но и значения полей модели, которая связана с запрошенной:
    # запрос №3
    # ice_cream_list = IceCream.objects.values('id', 'title', 'category__title')

    # Альтернатива запросу №3
    # В шаблоне можно получить доступ к полям связанного объекта через точечную нотацию:
    ice_cream_list = IceCream.objects.select_related('category').filter(id__lt=5)

    # Выводим запрос с сортировкой
    # Сортируем записи по значению поля output_order,
    # а если значения output_order у каких-то записей равны -
    # сортируем эти записи по названию в алфавитном порядке.
    # categories = Category.objects.values('id', 'output_order', 'title').order_by('output_order', 'title')

    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {'ice_cream_list': ice_cream_list}

    # передаем новый словарь
    # изменили шаблон т.к. передали новый словарь
    # context = {'categories': categories}
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template, context)
