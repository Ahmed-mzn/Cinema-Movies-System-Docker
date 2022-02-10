from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=55)
    short_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hour(models.Model):
    CHOICES_HOUR = (
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
        ('22:00', '22:00'),
        ('23:00', '23:00')
    )
    hour = models.CharField(max_length=20, choices=CHOICES_HOUR, unique=True)

    def __str__(self):
        return self.hour


class Movie(models.Model):

    CHOICES_RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    category = models.ForeignKey(Category, related_name='movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    hours = models.ManyToManyField(Hour)
    date = models.DateField()
    rating = models.IntegerField(choices=CHOICES_RATING, default=1)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'http://bulma.io/images/placeholders/1280x960.png'


class Booking(models.Model):
    ONLINE = 'online'
    CASH = 'cash'

    CHOICES_PAYMENT_TYPE = (
        (ONLINE, 'Online'),
        (CASH, 'Cash')
    )

    user = models.ForeignKey(User, related_name='bookings', on_delete=models.DO_NOTHING, blank=True, null=True)
    movie = models.ForeignKey(Movie, related_name='bookings', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    family_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    payment_type = models.CharField(max_length=25, choices=CHOICES_PAYMENT_TYPE, default=CASH)
    payed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
