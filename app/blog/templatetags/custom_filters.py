from django import template

register = template.Library()

@register.filter(name='my_custom_tag')
def my_custom_tag(argument_1):
    '''
        @register.simple_tag: este decorador registra la funcion como un template tag
        my_custom_tag: este es el nombre del tag que usaras en la plantilla
        Los argumentos que la funcion toma se pasaran desde la plantilla
    '''
    return "Php "+str(argument_1)


@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

#Truncar texto para mostrar solo las primeras x palabras
@register.filter(name='truncatewords')
def truncatewords(value, arg):
    words = value.split()
    return ' '.join(words[:arg])

#formate de fechas: crea un tag para mostrar la fecha de publicacion un post en formato legible ej: Publicado el 15 de enero de 2024
from datetime import datetime

@register.filter(name='date_public')
def date_public(value, format_string='%d de %m de %Y'):
    return datetime.strftime(value, format_string)

#formato de precio
@register.filter(name='format_price')
def format_price(value):
    return f'{value:,.2f}'

#Convertir la primera letra de cada palabra en mayuscula
@register.filter(name='upwords')
def upwords(value):
    result = ''
    words = [x for x in value.split(' ')]
    for word in words:
        result += f'{word.capitalize()} '
    return result

@register.inclusion_tag('categories.html')
def category(items):
    return {'category_items': items}


@register.inclusion_tag('product_detail.html')
def product_detail(product):
    return {'product':product}