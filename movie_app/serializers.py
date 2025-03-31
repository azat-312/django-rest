
from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError





class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies '.split()

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        depth = 1
        fields = 'title reviews'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist')
        return director_id



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(default=0)
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exist')
        return movie_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie = serializers.IntegerField()

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise serializers.ValidationError('Movie not found')
        return movie
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
