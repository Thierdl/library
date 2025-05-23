from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, BookForm
from .models import Category, Book



def list_category(request):
    category=Category.objects.all()
    return render(request, "category/list_category.html", {"category":category})



def add_category(request):

    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
           form.save()

           return redirect("/")
        
    else:
        form=CategoryForm()

    return  render(request, 'category/add_category.html', {"form":form})



def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method=="POST":
        name=request.POST.get('name')

        category.name=name

        category.save()
        return redirect("/")
    
    else:
        form = CategoryForm(instance=category)
    return render(request, "category/update_category.html", {"form":form, "category": category})





def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method=="POST":
        category.delete()
        return redirect("/")
    return render(request, "category/delete_category.html", {"category":category})




#---------------------------BOOK------------------------------

def list_book(request):
    #book = get_object_or_404(Book, id=book_id)
    books = Book.objects.all()
    return render(request, "book/list_book.html", {"books":books})




def add_book(request):

    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("list_book")
    else:
        form = BookForm()
    
    return render(request, "book/add_book.html", {"form":form})



def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method=="POST":
        category=request.POST.get("category")
        name=request.POST.get("name")
        book=request.FILES.get("book")

        category=Book.objects.get(id=category)

        book.category=category
        book.name=name
        book.book=book

        book.save()
        return redirect("/")
    
    form=BookForm()

    return render(request, "book/update_book.html", {"book":book, "form":form})



def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method=="POST":
        book.delete()
        return redirect("/")
    
    return render(request, "book/delete_book.html",{"book":book})
