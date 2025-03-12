from rest_framework import serializers
from .models import Director , Movie , Review



class DirectorDetailSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        field = ['name', 'movies_count']

    def get_movies_count(self, director):
        return director.movies.count()

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
      
        fields = 'name '.split()





class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
      
        fields = 'title description duration '.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
      
        fields = 'text'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class MoviesReviewsSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    reviews = ReviewDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['title', 'reviews', 'rating']

    def get_rating(self, movie):
        if movie.reviews.count() == 0:
            return 0
        else:
            reviews = movie.reviews.all()
            total = sum([review.stars for review in reviews if review.stars is not None])
            return total / movie.reviews.count()