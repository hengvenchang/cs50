from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from rating.models import Rating
from django.db.models import Avg
import requests


# Create your views here.
def index(request):
    user = request.user
    return render(request,'book/book.html',{'context':user})

def post(request):
    books = Book.objects.get(pk=request.GET.get("book_id"))
    return render(request,'book/search.html',{'book':books})

def search(request):
    search = request.GET.get('book_id')
    try:
        count = Book.objects.filter(title__icontains=search).count()
        books = Book.objects.filter(title__icontains=search)
    except KeyError:
        return HttpResponse("error")
    except Book.DoesNotExist:
        return HttpResponse("error Not Exist")
    if count >1:
        print('more')
    context = {
        'count': count,
        'books': books
    }
    print(count)
    return render(request,'book/search.html',{'context':context})
def show(request,book_id):
    try:
        book = Book.objects.get(pk=book_id)
        r = Rating.objects.filter(book_id=book_id)
        rating = r.aggregate(Avg('length'))
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "3KCBqjOpEOrBUkWfAxhwbQ" , "isbns" : book.isbn})
        res = res.json()
        res = res["books"]
    except KeyError:
        return HttpResponse("error")
    except Book.DoesNotExist:
        return HttpResponse("error Not Exist")
    context = {
    'user' : request.user,
    'book' : book,
    'rating': rating['length__avg'],
    'goodreads': res[0]['average_rating']
    }
    return render(request,'book/show.html',{'context':context})

# def rating(request):
#     rating_length = int(request.GET.get('rating_length'))
#     if(rating_length < 6):
#         # rating = Rating(length=rating_length)
#         # rating.user(request.seesion.user)
#         # rating.save()
#         rating = Rating.objects.get(pk=2)
#         # k = serializers.serialize('json', rating)
#         # dict_obj = model_to_dict( rating )
#         # return JsonResponse(k,safe=False)
#         # return jsonify(rating.serialize)
#         return HttpResponse(rating.user.all())
#         # return HttpResponse(json(rating))
#     return HttpResponse("no")
