from rest_framework import serializers
from .models import (
    Game, Rating, Genre,
    Publisher, Company, Developer,
    License, Award,
)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    rating = serializers.CharField()
    genres = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    publishers = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    companies = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    developers = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    awards = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    licenses = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = Game
        fields = '__all__'
