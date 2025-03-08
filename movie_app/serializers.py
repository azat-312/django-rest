from rest_framework import serializers
from .models import Director , Movie , Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
      
        fields = 'name '.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'



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