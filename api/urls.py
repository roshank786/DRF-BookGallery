from django.urls import path
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# created an object for DefaultRouter class

router.register("v1/books",views.BookViewSetView,basename="books")
# calling register method of DefaultRouter class

router.register("v1/reviews",views.ReviewUpdateDestroyViewSetView,basename="reviews")

urlpatterns = [

    path("books/",views.BookListCreateView.as_view()),

    path("books/<int:pk>/",views.BookRetrieveUpdateDeleteView.as_view()),

]+router.urls