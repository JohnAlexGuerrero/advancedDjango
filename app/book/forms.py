from django import forms

from book.models import Book, Category

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ("name","categories","published")
        widgets = {
            "categories": forms.CheckboxSelectMultiple(attrs={})
        }


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ("name",)

