from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer,DirectorValidateSerializer,MovieValidateSerializer,ReviewValidateSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
 
class DirectorListAPIView(ListCreateAPIView):
     queryset = Director.objects.all()
     serializer_class = DirectorSerializer

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
     queryset = Director.objects.all()
     serializer_class = DirectorDetailSerializer
     lookup_field = 'id'
 
 
class MovieListAPIView(ListAPIView):
     queryset = Movie.objects.all()
     serializer_class = MovieSerializer
class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
     queryset = Movie.objects.all()
     serializer_class = MovieSerializer
     lookup_field = 'id'
 
class ReviewsListAPIView(ListAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer
 
class ReviewsDetailAPIView(RetrieveUpdateDestroyAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer