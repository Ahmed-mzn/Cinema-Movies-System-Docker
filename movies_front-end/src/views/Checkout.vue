<template>
    <div class="checkout"><br><br><br>
        <v-form>
            <v-container>
                <v-row>
                    <v-col
                    cols="12"
                    sm="6"
                    >
                    <v-text-field
                        value="Movie:"
                        label="Solo"
                        solo
                        readonly
                    ></v-text-field>
                    </v-col>
                    <v-col
                    cols="12"
                    sm="6"
                    >
                    <v-text-field
                        :value="booking.movie.title"
                        label="Solo"
                        solo
                        readonly
                    ></v-text-field>
                    </v-col>

                    <v-col
                    cols="12"
                    sm="6"
                    >
                    <v-text-field
                        value="Full name:"
                        label="Solo"
                        solo
                        readonly
                    ></v-text-field>
                    </v-col>
                    <v-col
                    cols="12"
                    sm="6"
                    >
                    <v-text-field
                        :value="booking.first_name + ' ' + booking.last_name"
                        label="Solo"
                        solo
                        readonly
                    ></v-text-field>
                    </v-col>
                    
                    <v-col
                    cols="12"
                    sm="6"
                    >
                    <v-text-field
                        value="Date:"
                        label="Solo"
                        solo
                        readonly
                    ></v-text-field>
                    </v-col>
                    <v-col
                    cols="12"
                    sm="6"
                    >
                    <v-text-field
                        :value="booking.movie.date"
                        label="Solo"
                        solo
                        readonly
                    ></v-text-field>
                    </v-col>

                    <v-col
                    cols="12"
                    sm="6"
                    >

                    </v-col>
                    <v-col
                    cols="12"
                    sm="6"
                    >
                        <h2 v-if="booking.payed">Payed</h2>
                        <h2 v-else>Not payed</h2>
                    </v-col>
                    <v-col
                    cols="12"
                    sm="6"
                    >
                    <v-btn @click="print" color="blue"><v-icon>mdi-printer</v-icon>Imprimer</v-btn>
                    <v-btn to="/dashboard" class="ml-3"><v-icon>mdi-arrow-left</v-icon>Dashboard</v-btn>
                    </v-col>

                </v-row>
            </v-container>
        </v-form>
    </div>
</template>

<script>

import axios from 'axios'
export default {
    name: 'Checkout',
    data(){
        return {
            booking: null
        }
    },
    mounted(){
        this.getBooking()
    },
    methods:{
        getBooking(){
            var id = this.$route.params.id
            axios.get('/api/v1/get_booking/'+id)
            .then(response =>{
                this.booking = response.data
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        },
        print(){
            window.print()
        }
    }
}
</script>
