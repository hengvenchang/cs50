from django.urls import path
from . import views
from rating.views import RatingView,RatingDetailView
urlpatterns = [
    path("",RatingView.as_view()),
    path('<int:book_id>', views.RatingDetailView.as_view(), name='rating-detail'),
]
