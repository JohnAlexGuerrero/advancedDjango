from django.shortcuts import render
from datetime import datetime

from django.views.generic import TemplateView

# Create your views here.
class TutorialView(TemplateView):
    template_name = "tutorial.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_value"] = datetime(2024,9,12) 
        context["categories"] = [
            {"id":1, "name":'baloto'},
            {"id":2, "name":'baloto revancha'},
            {"id":3, "name":'miloto'},
            {"id":4, "name":'balotocolor'},
            
        ]
        context['description'] = '''
            ¡Absolutamente! Los filtros personalizados con template tags son una herramienta poderosa para manipular datos dentro de tus plantillas Django y personalizar la presentación de tu sitio web.

            ¿Qué es un filtro personalizado?

            Es una función de Python que se define dentro de un archivo de template tags y que se utiliza para transformar un valor antes de mostrarlo en la plantilla. Por ejemplo, puedes crear un filtro para:
        '''
        context['products'] = [
            {"id":1,"name": "alambre centelsa #12 verde","description":"conductor de cobre utilizado para las instalaciones electricas residenciales e industriales","price":2500},
            {"id":1,"name": "malla eslabonada 7x7 calibre 12","description":"malla para cerramiento de lotes","price":15500},
        ]
        return context
    
