from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Rating
from django.db.models import Avg
from django.views import View
import requests
class RatingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("jack hello")
    def post(self, request):
        try:
            user_id = request.POST.get("user_id")
            book_id = request.POST.get("book_id")
            length = request.POST.get("length")
            find = Rating.objects.filter(user_id=user_id, book_id=book_id)
            if not find :
                rating =  Rating.objects.update_or_create(user_id=user_id, book_id=book_id,length=length)
        except:
            return HttpResponse("error")
        return HttpResponse(length)
class RatingDetailView(View):
    def get(self, request, book_id):
        r = Rating.objects.filter(book_id=book_id)
        rating = r.aggregate(Avg('length'))
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "3KCBqjOpEOrBUkWfAxhwbQ" , "isbns" : "9781632168146"})
        res = res.json()
        res = res["books"]
        return HttpResponse(res[0]['average_rating'])
    def post(self, request,book_id):
        return HttpResponse(book_id)
