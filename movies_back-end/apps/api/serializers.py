from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Movie, Hour, Booking


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'short_description', 'created_at')


class HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour
        fields = ('id', 'hour')


class MovieSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    hours = HourSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        read_only_fields = (
            "image",
        )
        fields = ('id', 'title', 'category', 'short_description', 'long_description', 'rating', 'hours', 'date',
                  'get_image', 'created_at')


class BookingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False, read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'movie', 'first_name', 'last_name', 'family_name', 'email', 'phone_number', 'payment_type',
                  'payed', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
