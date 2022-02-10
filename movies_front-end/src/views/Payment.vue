<template>
    <section id="hero">
        <v-parallax dark src="@/assets/img/money.jpg" height="750">
            <v-row align="center" justify="center">
                <v-col cols="10">
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
                        <v-col cols="12" sm="9">
                            <h1 class="display-2 font-weight-bold mb-4">Payment</h1>
                                <div v-if="!paidFor">
                                    <h1>Booking movie '{{booking.movie.title}}' - ${{ product.price }} </h1>

                                    <p>{{ booking.movie.short_description }}</p>
                                    <p><strong>Date :</strong> {{booking.movie.date}}</p>

                                </div>

                                <div v-if="paidFor">
                                    <h1>Payment est fait avec succès</h1>
                                </div>

                                <div ref="paypal"></div>
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
        <br><br>
        <div class="svg-border-waves">
            <img src="~@/assets/img/wave2.svg" />
        </div>
        <v-snackbar
            v-model="snackbar"
            color="success"
            timeout="3000"
        >
        Payment est fait avec succès

            <template v-slot:action="{ attrs }">
                <v-btn
                    color="pink"
                    text
                    v-bind="attrs"
                    @click="snackbar = false"
                >
                Close
                </v-btn>
            </template>
        </v-snackbar>
    </section>
</template>

<script>

import axios from 'axios'
export default {
    name: 'Payment',
    data(){
        return{
            loaded: false,
            paidFor: false,
            snackbar: false,
            product: {
                price: 200,
                description: "leg lamp from that one movie",
                img: "./assets/lamp.jpg"
            },
            booking: null
        }
    },
    mounted: function() {
        this.getBooking()
        const script = document.createElement("script");
        script.src =
        "https://www.paypal.com/sdk/js?client-id=AcNteclFS8r6Aj21Nya9wS7P2c_ZV0U7axcXdPQgPozTnVDly7GtPjr09ThTWwtAPkFXm60mwZeooOtb";
        script.addEventListener("load", this.setLoaded);
        document.body.appendChild(script);
    },
    methods: {
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
        setLoaded: function() {
        this.loaded = true;
        window.paypal
            .Buttons({
                createOrder: (data, actions) => {
                    return actions.order.create({
                    purchase_units: [
                        {
                        description: this.product.description,
                        amount: {
                            currency_code: "USD",
                            value: this.product.price
                        }
                        }
                    ]
                    });
                },
                onApprove: async (data, actions) => {
                    const order = await actions.order.capture();
                    this.paidFor = true;
                    this.snackbar = true
                    axios.post('/api/v1/set_booking_payed/'+this.booking.id)
                    .then(() =>{
                        console.log(order)
                        this.$router.push('/checkout/'+this.booking.id)
                    })
                    .catch(error =>{
                        console.log(JSON.stringify(error))
                    })
                },
                onError: err => {
                    console.log(err);
                }
            })
            .render(this.$refs.paypal);
        }
    }
}
</script>
