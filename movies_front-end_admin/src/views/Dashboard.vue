<template>
    <div class="dahsboard">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Dashboard</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-10 is-offset-1">
                        <nav class="breadcrumb" aria-label="breadcrumbs">
                            <ul>
                                <li><a href="/">CW Admin App</a></li>
                                <li><a href="/dashboard">Dashboard</a></li>
                                <li class="is-active"><a href="#" aria-current="page">Admin</a></li>
                            </ul>
                        </nav>
                        <section class="hero is-info welcome is-small">
                            <div class="hero-body">
                                <div class="container">
                                    <h1 class="title">
                                        Hello, Admin.
                                    </h1>
                                    <h2 class="subtitle">
                                        I hope you are having a great day!
                                    </h2>
                                </div>
                            </div>
                        </section><br>
                        <section class="info-tiles">
                            <div class="tile is-ancestor has-text-centered">
                                <div class="tile is-parent">
                                    <article class="tile is-child box">
                                        <p class="title">{{dashboard.users}}k</p>
                                        <p class="subtitle">Users</p>
                                    </article>
                                </div>
                                <div class="tile is-parent">
                                    <article class="tile is-child box">
                                        <p class="title">{{dashboard.movies}}k</p>
                                        <p class="subtitle">Movies</p>
                                    </article>
                                </div>
                                <div class="tile is-parent">
                                    <article class="tile is-child box">
                                        <p class="title">3.4k</p>
                                        <p class="subtitle">visits</p>
                                    </article>
                                </div>
                                <div class="tile is-parent">
                                    <article class="tile is-child box">
                                        <p class="title">{{dashboard.bookings}}</p>
                                        <p class="subtitle">Bookings</p>
                                    </article>
                                </div>
                            </div>
                        </section><br>
                        <div class="columns">
                            <div class="column is-6">
                                <div class="card events-card">
                                    <header class="card-header">
                                        <p class="card-header-title">
                                            Last bookings
                                        </p>
                                        <a href="#" class="card-header-icon" aria-label="more options">
                                            <span class="icon">
                                                <i class="fa fa-angle-down" aria-hidden="true"></i>
                                            </span>
                                        </a>
                                    </header>
                                    <div class="card-table">
                                        <div class="content">
                                            <table class="table is-fullwidth is-striped is-hoverable">
                                                <tbody>
                                                    <tr
                                                        v-for="booking in bookings"
                                                        :key="booking.id"
                                                    >
                                                        <td width="5%"><i class="fa fa-bell-o"></i></td>
                                                        <td><b>{{booking.first_name}} {{booking.last_name}}</b> - {{booking.movie.title}}</td>
                                                        <td class="level-right">
                                                                <template v-if="booking.payed">
                                                                    <span class="pl-3 has-text-success is-size-5"><fa :icon="['fas', 'check-circle']"/></span>
                                                                </template>
                                                                <template v-else>
                                                                    <span class="pl-3 has-text-danger is-size-5"><fa :icon="['fas', 'times-circle']"/></span>
                                                                </template>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                    <footer class="card-footer">
                                        <a href="/bookings" class="card-footer-item">View All</a>
                                    </footer>
                                </div>
                            </div>
                            <div class="column is-6">
                                <div class="card">
                                    <header class="card-header">
                                        <p class="card-header-title">
                                            Movie Search
                                        </p>
                                        <a href="#" class="card-header-icon" aria-label="more options">
                                            <span class="icon">
                                                <i class="fa fa-angle-down" aria-hidden="true"></i>
                                            </span>
                                        </a>
                                    </header>
                                    <div class="card-content">
                                        <div class="content">
                                            <div class="control has-icons-left has-icons-right">
                                                <input class="input is-large" type="text" placeholder="">
                                                <span class="icon is-medium is-left">
                                                    <i class="fa fa-search"></i>
                                                </span>
                                                <span class="icon is-medium is-right">
                                                    <i class="fa fa-check"></i>
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="card">
                                    <header class="card-header">
                                        <p class="card-header-title">
                                            User Search
                                        </p>
                                        <a href="#" class="card-header-icon" aria-label="more options">
                                            <span class="icon">
                                                <i class="fa fa-angle-down" aria-hidden="true"></i>
                                            </span>
                                        </a>
                                    </header>
                                    <div class="card-content">
                                        <div class="content">
                                            <div class="control has-icons-left has-icons-right">
                                                <input class="input is-large" type="text" placeholder="">
                                                <span class="icon is-medium is-left">
                                                    <i class="fa fa-search"></i>
                                                </span>
                                                <span class="icon is-medium is-right">
                                                    <i class="fa fa-check"></i>
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Dashboard',
    data(){
        return{
            dashboard: {
                users: 0,
                movies: 0,
                bookings: 0
            },
            bookings:[]
        }
    },
    mounted(){
        this.getBookings()
        this.getDashboard()
    },
    methods:{
        getBookings(){
            axios.get('/api/v1/bookings')
            .then(response =>{
                if(response.data.length > 7) {
                    for(let i=0; i<7; i++){
                        this.bookings.push(response.data[i]);
                    }
                } else {
                    this.bookings = response.data
                }
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        },
        getDashboard(){
            axios.get('/api/v1/get_dashboard')
            .then(response =>{
                this.dashboard.users = response.data.data.users
                this.dashboard.movies = response.data.data.movies
                this.dashboard.bookings = response.data.data.bookings
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        }
    }
}
</script>
