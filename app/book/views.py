from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView

from book.resources import BookResources

from book.models import Book, Category
from book.forms import BookForm, CategoryForm

# Create your views here.
class BookCreateView(CreateView):
    model = Book
    template_name = "book/form.html"
    form_class = BookForm
    success_url = reverse_lazy('list_book')

class BookListView(ListView):
    model = Book
    template_name = "book/list.html"
    
    def get_queryset(self):
        return super().get_queryset()

class BookUpdateView(UpdateView):
    model = Book
    template_name = "book/form.html"
    form_class = BookForm
    success_url = reverse_lazy('list_book')

    
    
    
# Create your views here.
class CategoryCreateView(CreateView):
    model = Category
    template_name = "category/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('list_category')

class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"


#export csv
def export_csv(request):
    dataset = BookResources().export()
    print(dataset.csv)
    
    return redirect('list_book')