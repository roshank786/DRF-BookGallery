from rest_framework import serializers
# serializers are used to convert query set to python native language and vice versa
from api.models import Book,Review





class ReviewSerializer(serializers.ModelSerializer):

    book_object = serializers.StringRelatedField()

    class Meta:

        model = Review

        fields = "__all__"

        read_only_fields = ["id","book_object"]
        # giving these as read only, otherwise while creating these two fields will required to be passed body along with
        # other fields like comment,rating,user



class BookSerializers(serializers.ModelSerializer):

    # reviews = ReviewSerializer(read_only=True,many=True)
    reviews = serializers.SerializerMethodField(read_only = True)


    # review_count = serializers.CharField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    
    # avg_rating = serializers.CharField(read_only=True)
    avg_rating = serializers.SerializerMethodField(read_only=True)

    
    class Meta:

        model = Book
        
        # fields = "__all__"
        # to add all the fields

        fields = ["id","title","author","genre","price","language","reviews","review_count","avg_rating"]



    # another method for counting reviews
    # get should be always given as prefix if writing a custom method as SerializerMethodField()
    def get_review_count(self,obj):

        return Review.objects.filter(book_object = obj).count()
    
    def get_avg_rating(self,obj):

        reviews = Review.objects.filter(book_object = obj)
        avg = 0
        if reviews:
            avg = sum([r.rating for r in reviews])/reviews.count()
            # OR
            # avg = sum([r.rating for r in reviews])/self.get_review_count(obj)
        
        return avg
    
    
    def get_reviews(self,obj):

        qs = Review.objects.filter(book_object=obj)

        serializer_instance = ReviewSerializer(qs,many=True)
        # converting qs into python native type

        return serializer_instance.data