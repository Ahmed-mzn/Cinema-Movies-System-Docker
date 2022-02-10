import os
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Category, Movie, Booking, Hour
from .serializers import CategorySerializer, MovieSerializer, HourSerializer, BookingSerializer, UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        return self.queryset.filter(user=self.request.user)


class HourViewSet(viewsets.ModelViewSet):
    serializer_class = HourSerializer
    queryset = Hour.objects.all()


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_movie(request):
    category = Category.objects.get(pk=request.data['category'])

    movie = Movie.objects.create(image=request.data['image'], category=category, title=request.data['title'],
                                 short_description=request.data['short_description'], date=datetime.now().date(),
                                 rating=request.data['rating'])

    serializer = MovieSerializer(movie)

    return Response(
        {
            "status": "success",
            "data": serializer.data
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.short_description = request.data['short_description']
    movie.title = request.data['title']
    movie.rating = request.data['rating']
    movie.category = Category.objects.get(pk=request.data['category'])
    movie.date = request.data['date']

    print(request.data['img_changed'])

    if int(request.data['img_changed']) == 1:
        print('oui')
        # deleting old uploaded image.
        try:
            image_path = movie.image.url
            print(image_path)
            if os.path.exists(image_path):
                os.remove(image_path)
        except:
            pass
        movie.image = request.data['image']
    movie.save()

    serializer = MovieSerializer(movie)

    return Response(
        {
            "status": "success",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_hours(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.hours.clear()
    for hour in request.data['hours']:
        hour = Hour.objects.get(hour=hour)
        movie.hours.add(hour)

    serializer = MovieSerializer(movie)

    return Response(
        {
            "status": "success",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def assigned_hours(request):
    movie = Movie.objects.get(pk=request.data['movie'])
    for hour in request.data['hours']:
        hour = Hour.objects.get(hour=hour)
        movie.hours.add(hour)

    serializer = MovieSerializer(movie)
    return Response(
        {
            "status": "success",
            "data": serializer.data
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_dashboard(request):
    users = User.objects.count()
    movies = Movie.objects.count()
    bookings = Booking.objects.count()

    return Response(
        {
            "status": "success",
            "data": {
                "users": users,
                "movies": movies,
                "bookings": bookings
            }
        }
    )


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_hours(request):
    hours = Hour.objects.all()
    serializer = HourSerializer(hours, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_booking(request):
    if request.user:
        movie = Movie.objects.get(pk=request.data['movie'])
        user = User.objects.get(pk=request.data['user'])
        booking = Booking.objects.create(movie=movie, user=user, last_name=user.last_name,
                                         first_name=user.first_name, email=user.email,
                                         payment_type=request.data['payment_type'], payed=False)
    else:
        movie = Movie.objects.get(pk=request.data['movie'])
        booking = Booking.objects.create(movie=movie, first_name=request.data['first_name'],
                                     last_name=request.data['last_name'], family_name=request.data['family_name'],
                                     email=request.data['email'], phone_number=request.data['phone_number'],
                                     payment_type=request.data['payment_type'], payed=request.data['payed'])

    if booking:
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def set_booking_payed(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.payed = True
    booking.payment_type = Booking.ONLINE
    booking.save()
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_200_OK)