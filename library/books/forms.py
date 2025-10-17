from django import forms

# class BooksForm(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     pages=forms.IntegerField()
#     price=forms.IntegerField()
#     language=forms.CharField()

from books.models import Book
class BooksForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'