'''
El widget ManyToMany es un widget que convierte entre representaciones de una relación
ManyToMany como una lista y un campo ManyToMany real.

parameters:
    model
    separator - default ","
    field default pk
    
'''

from import_export import resources
from book.models import Category, Book
from import_export.widgets import ManyToManyWidget
from import_export.fields import Field

class BookResources(resources.ModelResource):
    categories = Field(
        column_name='categories',
        attribute='categories',
        widget=ManyToManyWidget(model=Category, separator=',', field='name')
    )
    
    class Meta:
        model = Book
