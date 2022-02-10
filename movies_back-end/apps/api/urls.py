from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, MovieViewSet, BookingViewSet, HourViewSet,\
    get_categories, get_hours, get_movies, add_booking, create_user, get_booking,\
    set_booking_payed, add_movie, assigned_hours, update_movie, update_hours, get_dashboard

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('movies', MovieViewSet, basename='movies')
router.register('hours', HourViewSet, basename='hours')
router.register('bookings', BookingViewSet, basename='bookings')


urlpatterns = [
    path('', include(router.urls)),
    path('get_categories', get_categories),
    path('get_dashboard', get_dashboard),
    path('get_hours', get_hours),
    path('add_movie', add_movie),
    path('update_movie/<int:pk>', update_movie),
    path('update_hours/<int:pk>', update_hours),
    path('assigned_hours', assigned_hours),
    path('get_movies', get_movies),
    path('add_booking', add_booking),
    path('create_user', create_user),
    path('get_booking/<int:pk>', get_booking),
    path('set_booking_payed/<int:pk>', set_booking_payed),
]