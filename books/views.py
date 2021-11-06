
from django.shortcuts import redirect, render
from .forms import BookFormSet,BookForm
from .models import Author,Book
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def books(request):
    books=Book.objects.all()
    return render(request,"partials/books.html",{"books":books})
def create_book_form(request):
    form = BookForm()
    context = {
        "form": form
    }
    return render(request, "partials/book_form.html", context)

def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book=form.save(commit=False)
            book.author=author
            book.save()
            
            return redirect("detail-book",pk=book.id)
        else:
            return render(request,"partials/book_form.html",context={"form":form})

    context = {
        "form": form,
        "author": author,
        "books": books
    }

    return render(request, "create_book.html", context)

def detail_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)

def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-book", pk=book.id)

    context = {
        "form": form,
        "book": book
    }

    return render(request, "partials/book_form.html", context)

def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "POST":
        book.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )