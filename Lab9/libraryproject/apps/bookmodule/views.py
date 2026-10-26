from django.shortcuts import render
from django.http import HttpResponse 
from .models import Book, Student, Publisher

from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import F, FloatField, Value, ExpressionWrapper
from django.db.models import OuterRef, Subquery

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name}) 

def index2(request, val1 = 0):
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId): 
    # assume that we have the following books somewhere (e.g. database) 
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'} 
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    targetBook = None 
    if book1['id'] == bookId: targetBook = book1 
    if book2['id'] == bookId: targetBook = book2 
    context = {'book':targetBook} # book is the variable name accessible by the template 
    return render(request, 'bookmodule/show.html', context) 

def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3] 

def index(request): 
    return render(request, "bookmodule/index.html") 
  
def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 
  
def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 
  
def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html') 

def links(request): 
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST": 
        string = request.POST.get('keyword').lower() 
        isTitle = request.POST.get('option1') 
        isAuthor = request.POST.get('option2') 
        # now filter 
        books = __getBooksList() 
        newBooks = [] 
        for item in books: 
            contained = False 
            if isTitle and string in item['title'].lower(): contained = True 
            if not contained and isAuthor and string in item['author'].lower():contained = True 

            if contained: newBooks.append(item) 
        return render(request, 'bookmodule/bookList.html', {'books':newBooks}) 
    return render(request, 'bookmodule/search.html')


def lab8_task7(request):
    cities = Student.objects.values('address__city').annotate(
        student_count=Count('id')
    ).order_by('address__city')

    return render(request, 'bookmodule/lab8_task7.html', {'cities': cities})


def lab9_task1(request):
    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 0

    if total_quantity > 0:
        books = Book.objects.annotate(
            availability_percentage=ExpressionWrapper(
                F('quantity') * Value(100.0) / Value(total_quantity),
                output_field=FloatField()
            )
        )
    else:
        books = Book.objects.annotate(
            availability_percentage=Value(0.0, output_field=FloatField())
        )
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(
        total_stock=Sum('book__quantity')
    )

    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})


def lab9_task3(request):
    oldest_books = Book.objects.filter(
        publisher=OuterRef('pk')
    ).order_by('pubdate', 'pk')

    publishers = Publisher.objects.annotate(
        oldest_book_title=Subquery(
            oldest_books.values('title')[:1]
        ),
        oldest_pubdate=Min('book__pubdate')
    )

    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )

    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})


def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        highly_rated_count=Count(
            'book',
            filter=Q(book__rating=5)
        )
    )

    for publisher in publishers:
        publisher.highly_rated_books = Book.objects.filter(
            publisher=publisher,
            rating=5
        )

    return render(
        request,
        'bookmodule/lab9_task5.html',
        {'publishers': publishers}
    )


def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        matching_books_count=Count(
            'book',
            filter=Q(
                book__price__gt=50,
                book__quantity__gte=1,
                book__quantity__lt=5
            )))

    return render(
        request,
        'bookmodule/lab9_task6.html',
        {'publishers': publishers}
    )

