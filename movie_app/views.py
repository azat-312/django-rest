from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorDetailSerializer, MoviesReviewsSerializer ,MovieDetailSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
 



class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
    


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


class MoviesReviewsListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesReviewsSerializer
    pagination_class = CustomPagination

def movies_reviews_list_api_view(request):
     movies = Movie.objects.all()
     data = MoviesReviewsSerializer(movies, many=True).data
     return Response(data=data)      