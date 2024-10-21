from django.urls import path

from book.views import BookCreateView, BookListView, CategoryCreateView, CategoryListView, BookUpdateView
from book.views import export_csv

urlpatterns = [
    path('list/', BookListView.as_view(), name='list_book'),
    path('new/', BookCreateView.as_view(), name='create_book'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='edit_book'),
    # category
    path('category/list/', CategoryListView.as_view(), name='list_category'),
    path('category/new/', CategoryCreateView.as_view(), name='create_category'),
    #export CSV
    path('export-csv/', export_csv, name='export_dataset_book'),
]
