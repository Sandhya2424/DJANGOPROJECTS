from django.shortcuts import render, redirect

from books.forms import BooksForm

#class based view

from django.views import View

class Home(View):
    def get(self,request):
        return render(request,'home.html')

from books.models import Book

class Addbooks(View):
    def post(self,request):
        print(request.POST)
        print(request.FILES)
        form_instance = BooksForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:viewbooks')
    def get(self,request):
        form_instance = BooksForm()
        context = {'form': form_instance}
        return render(request, 'addbooks.html', context)


class Viewbooks(View):
    def get(self, request):
        b=Book.objects.all()
        context={'books': b}
        return render(request, 'viewbooks.html', {'books': b})


class Bookdetail(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        context = {'books': b}
        return render(request, 'bookdetail.html', context)


class Editbook(View):
    def post(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = BooksForm(request.POST, request.FILES, instance=b)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('books:viewbooks')
    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=BooksForm(instance=b)
        context={'form': form_instance}
        return render(request, 'editbook.html', context)


class Deletebook(View):
    def get(self, request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')

from django.db.models import Q
class Searchbook(View):
    def get(self, request):
        query=request.GET['q']
        # print(query)
        if query:
            b=Book.objects.filter(Q(author__icontains=query)|Q(title__icontains=query)|Q(language__icontains=query))
            #Q Object --> syntax used to add logical or /logical and in orm queries
            #field lookups --> fieldname__lookup eg:age__gt=30/ age__lt=30/title__icontains
            context={'books':b}
            return render(request, 'search.html',context)
