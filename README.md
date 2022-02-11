# Cinema-Movies-System-Docker


# Description 
This system is for manage a cinema, its consists of three apps :


# API where we have all services those communicate with database :
#### Technologies : 
- Django
- PostgreSQL

#### Services :
- Authentication (with Tokens) / Authorization
- Categories services
- Movies services
- Users services
- Bookings services
- Payment procedure

# Front-end public app
#### Technologies : 
- Nodejs
- Vue js
- Vuetify

#### Services :
- Home page
- About
- Contact
- Movies
- Login/Sign up
- Booking
- Dashboard (For those users having an account )
- Payment for a booking

# Front-end admin app
#### Technologies : 
- Nodejs
- Vue js
- Bulma

#### Services :
We can acces for all services of API

# Installation

### Requirements :
- Docker (with docker-compose)



### Commands for running apps :
```bash
$ docker-compose run movies_back-end python manage.py makemigrations
```



```bash
$ docker-compose run movies_back-end python manage.py migrate
```


#### Now create a super user for manage the database

```bash
$ docker-compose run movies_back-end python manage.py createsuperuser
```



```bash
$ docker-compose up
```

### Apps links :
- 0.0.0.0:8000/admin ---> django admin
- 127.0.0.1:8181 ---> public app
- 127.0.0.1:8282 ---> admin app

Enjoy !


## Issues

When you have an error related with docker-compose version just change the version of docker-compose in the docker-compose.yml file to an old version 3.0 or 2.*






