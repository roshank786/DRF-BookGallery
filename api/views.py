from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
# response is to convert python native components to JSON

from rest_framework import viewsets

from api.serializers import BookSerializers,ReviewSerializer

from api.models import Book,Review

from rest_framework.decorators import action
# Create your views here.



class BookListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs = Book.objects.all()

        serializer_instance = BookSerializers(qs,many = True)
        # if its query set, then qs to py native is serializeration

        return Response(data=serializer_instance.data)
    

    def post(self,request,*args,**kwargs):

        serializer_instance = BookSerializers(data=request.data)
        # if its data, then py native to qs is deserializeration

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
    

class BookRetrieveUpdateDeleteView(APIView):



    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = Book.objects.get(id=id)

        serializer_instance = BookSerializers(qs)

        return Response(data=serializer_instance.data)
    
    def put(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        book_obj = Book.objects.get(id=id)

        serializer_instance = BookSerializers(data=request.data,instance=book_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
    
    def delete(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        Book.objects.get(id=id).delete()

        data = {"message":"data deleted"}

        return Response(data)
    






class BookViewSetView(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):

        qs = Book.objects.all()

        serialzer_instance = BookSerializers(qs,many=True)

        return Response(data=serialzer_instance.data)
    
    
    def create(self,request,*args,**kwargs):

        serializer_instance = BookSerializers(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

    def retrieve(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = Book.objects.get(id=id)

        serializer_instance  = BookSerializers(qs)

        return Response(data=serializer_instance.data)
    

    def update(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        book_obj = Book.objects.get(id=id)

        serializer_instance = BookSerializers(data=request.data,instance=book_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    
    def destroy(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        Book.objects.get(id=id).delete()

        data = {"message":"deleted"}

        return Response(data=data)
    


    @action(methods=["GET"],detail=False)
    def authors_list(self,request,*args,**kwargs):

        authors = Book.objects.all().values_list("author",flat=True).distinct()

        return Response(data=authors)
    

    @action(methods=["GET"],detail=False)
    def genre_list(self,request,*args,**kwargs):

        genres = Book.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=genres)
    

    # url:lh:8000/api/books/{id}/add_review/
    # method:post


    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):

        book_id = kwargs.get("pk")

        book_obj = Book.objects.get(id=book_id)

        serializer_instance = ReviewSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(book_object=book_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

class ReviewUpdateDestroyViewSetView(viewsets.ViewSet):

    def destroy(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        Review.objects.get(id=id).delete()

        data = {"message":"deleted review"}

        return Response(data)
    
    def update(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        review_obj = Review.objects.get(id=id)

        serializer_instance = ReviewSerializer(data=request.data,instance=review_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        



    def retrieve(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = Review.objects.get(id=id)

        serializer_instance = ReviewSerializer(qs)

        return Response(data=serializer_instance.data)