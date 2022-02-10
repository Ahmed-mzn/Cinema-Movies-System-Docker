<template>
    <div class="hero is-info">
        <div class="hero-body has-text-centered">
            <h1 class="title">Reservations</h1>
        </div>
    </div>

    <br>
    <section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-12">
                    <table id="myTable" class="table is-fullwidth is-hoverable">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>First Name</th>
                                <th>Last Name</th>
                                <th>Email</th>
                                <th>Movie</th>
                                <th>Movie Date</th>
                                <th>Payment Type</th>
                                <th>Payed</th>
                                <th>Action</th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="booking in bookings"
                                :key="booking.id"
                            >
                                <th>{{booking.id}}</th>
                                <td>{{booking.first_name}}</td>
                                <td>{{booking.last_name}}</td>
                                <td>{{booking.email}}</td>
                                <td>{{booking.movie.title}}</td>
                                <td>{{booking.movie.date}}</td>
                                <td>{{booking.payment_type}}</td>
                                <th>
                                    <template v-if="booking.payed">
                                        <span class="pl-3 has-text-success is-size-5"><fa :icon="['fas', 'check-circle']"/></span>
                                    </template>
                                    <template v-else>
                                        <span class="pl-3 has-text-danger is-size-5"><fa :icon="['fas', 'times-circle']"/></span>
                                    </template>
                                </th>
                                <td>
                                    <div class="buttons">
                                        <a @click="ShowDeleteModal(booking.id)" class="button is-danger is-inverted"><span><fa :icon="['far', 'trash-alt']"/></span></a>
                                        <a @click="ShowEditModal(booking)" class="button is-info is-inverted">
                                            <span><fa :icon="['far', 'edit']"/></span>
                                        </a>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </section>
    <br>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Bookings',
    data(){
        return{
            bookings:[]
        }
    },
    mounted(){
        this.getBookings()
    },
    methods:{
        getBookings(){
            axios.get('/api/v1/bookings')
            .then(response =>{
                this.bookings = response.data
                $(document).ready(function() {
                    $('#myTable').DataTable();
                } );
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        }
    }
}
</script>
