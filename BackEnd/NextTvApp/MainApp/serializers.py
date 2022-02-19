from rest_framework import serializers
from .models import MovieTitle, Contestants, Nominations, Category


class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTitle
        fields = '__all__'



class NominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominations
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



