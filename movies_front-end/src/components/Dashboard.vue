<template>
    <section id="hero">
        <v-parallax dark src="@/assets/img/about.jpg" height="750">
            <v-row align="center" justify="center">
                <v-col cols="10">
                    <v-row align="center" justify="center">
                        <v-col cols="12" md="6" xl="8">
                            <h1 class="display-2 font-weight-bold mb-4">Dashboard</h1>
                            <h1 class="font-weight-light">
                                We have a simple dashborad with last bookings <br />
                                adipisicing elit. Maiores porro voluptatibus <br />
                                delectus nam optio harum!
                            </h1>
                        </v-col>
                        <v-col cols="12" md="6" xl="4" class="hidden-sm-and-down"> </v-col>
                    </v-row>
                </v-col>
            </v-row>
            <div class="svg-border-waves text-white">
                <v-img src="@/assets/img/borderWaves.svg" />
            </div>
        </v-parallax>
        <v-container fluid id="features" class="mt-2">
            <v-row align="center" justify="center">
                <v-col cols="10">
                    <v-row align="center" justify="space-around">
                        <v-col cols="12" sm="11">
                        <h1 class="display-2 font-weight-bold mb-4">Bookings</h1>
                            <v-card>
                                <v-card-title>
                                    <v-text-field
                                        v-model="search"
                                        append-icon="mdi-magnify"
                                        label="Search"
                                        single-line
                                        hide-details
                                    ></v-text-field>
                                </v-card-title>
                                <v-data-table
                                    :headers="headers"
                                    :items="bookings"
                                    :search="search"
                                >
                                    <template v-slot:item.payed="{ item }">
                                        <v-icon
                                            v-if="item.payed"
                                            color="success"
                                        >mdi-check-bold</v-icon>
                                        <v-icon
                                            v-else
                                            color="red"
                                        >mdi-close-thick</v-icon>
                                    </template>
                                    <template v-slot:item.created_at="{ item }">
                                        {{formatDate(item.created_at)}}
                                    </template>
                                    <template v-slot:item.actions="{ item }">
                                        <v-icon
                                            small
                                            class="mr-2"
                                            @click="$router.push('/checkout/'+item.id)"
                                        >
                                            mdi-eye
                                        </v-icon>
                                        <v-icon
                                        v-if="!item.payed"
                                            small
                                            class="mr-2"
                                            @click="$router.push('/payment/'+item.id)"
                                        >
                                            mdi-credit-card-outline
                                        </v-icon>
                                    </template>
                                </v-data-table>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
        <br><br>
        <div class="svg-border-waves">
            <img src="~@/assets/img/wave2.svg" />
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
export default {
    data() {
        return {
            search: '',
            headers: [
                { text: 'ID', value: 'id' },
                {
                    text: 'Movie',
                    align: 'start',
                    value: 'movie.title',
                },
                { text: 'Movie Date', value: 'movie.date' },
                { text: 'Payment Type', value: 'payment_type' },
                { text: 'Payed', value: 'payed' },
                { text: 'Date', value: 'created_at' },
                { text: 'Actions', value: 'actions', sortable: false },
            ],
            bookings: [],
        }
    },
    mounted(){
        this.getBookings()
    },
    watch: {
        dialog(value) {
            if (!value) {
                this.pause();
            }
        },
    },
    methods: {
        formatDate(date){
            return moment(date).locale('fr').format('LLL')
        },
        getBookings(){
            axios.get('/api/v1/bookings')
            .then(response =>{
                this.bookings = response.data
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        }
    },
};
</script>
