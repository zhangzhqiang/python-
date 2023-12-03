from django.shortcuts import render, HttpResponse, redirect
from book.models import Book


# Create your views here.

def addbook(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        book_obj = Book.objects.create(title=title, price=price, pub_date=date, publish=publish)
        print(book_obj)
        return redirect("/books")
    return render(request, "addbook.html")


def books(request):
    book_list = Book.objects.all()
    book1 = Book.objects.all().first()
    print(book1)
    return render(request, 'books.html', locals())
