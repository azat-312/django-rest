from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director , Movie , Review
from .serializers import (DirectorSerializer,DirectorDetailSerializer,
MovieSerializer,MovieDetailSerializer,ReviewSerializer,ReviewDetailSerializer)

@api_view(http_method_names=['GET'])
def director_api_view(request):
    # step 1: Collect products from DB (QuerySet)
    director = Director.objects.filter()

    # step 2: Reformat QuerySet to list of dictionary (Serializer)
    data = DirectorSerializer(director, many=True).data

    # step 3: Return Response
    return Response(data=data)  # data = dict / list / list of dict


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorDetailSerializer(director, many=False).data
    return Response(data=data)




@api_view(http_method_names=['GET'])
def movie_api_view(request):
    # step 1: Collect products from DB (QuerySet)
    movie = Movie.objects.filter()

    # step 2: Reformat QuerySet to list of dictionary (Serializer)
    data = MovieSerializer(movie, many=True).data

    # step 3: Return Response
    return Response(data=data)  # data = dict / list / list of dict


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieDetailSerializer(movie, many=False).data
    return Response(data=data)




@api_view(http_method_names=['GET'])
def review_api_view(request):
    # step 1: Collect products from DB (QuerySet)
    review = Review.objects.filter()

    # step 2: Reformat QuerySet to list of dictionary (Serializer)
    data = ReviewSerializer(review, many=True).data

    # step 3: Return Response
    return Response(data=data)  # data = dict / list / list of dict


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)

