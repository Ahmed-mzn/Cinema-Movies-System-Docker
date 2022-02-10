<template>
    <section id="hero">
        <v-parallax dark src="@/assets/img/about.jpg" height="750">
            <v-row align="center" justify="center">
                <v-col cols="10">
                    <v-row align="center" justify="center">
                        <v-col cols="12" md="6" xl="8">
                            <h1 class="display-2 font-weight-bold mb-4">Connecter</h1>
                            <h1 class="font-weight-light">
                                This log in able you to booking movies online <br />
                                you can get all old bookings <br />
                                and also more thinks...
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
                            <h1 class="display-2 font-weight-bold mb-4">Se Connecter</h1>
                            <v-form ref="form" v-model="valid" :lazy-validation="lazy">
                                <v-text-field
                                    v-model="user.username"
                                    :rules="emailRules"
                                    label="E-mail"
                                    required
                                ></v-text-field>

                                <v-text-field
                                    v-model="user.password"
                                    :rules="nameRules"
                                    type="password"
                                    label="Mot de passe"
                                    required
                                ></v-text-field>

                                <v-btn
                                    :disabled="!valid"
                                    color="primary"
                                    :dark="valid"
                                    rounded
                                    block
                                    class="mt-3"
                                    @click="submit"
                                >
                                Connecter
                                </v-btn>
                            </v-form>
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
            v-model="snackbar.enabled"
            :color="snackbar.color"
            timeout="3000"
        >
        {{ snackbar.text }}

        <template v-slot:action="{ attrs }">
            <v-btn
                color="pink"
                text
                v-bind="attrs"
                @click="snackbar.enabled = false"
            >
            Close
            </v-btn>
        </template>
        </v-snackbar>
    </section>
</template>

<script>
import axios from 'axios'
import Form from 'vform'
export default {
    data: () => ({
        user: new Form({
            username: '',
            password: ''
        }),
        valid: true,
        nameRules: [
            (v) => !!v || "Champ mot de passe est obligatoire",
        ],
        emailRules: [
            (v) => !!v || "Champ email est obligatoire",
            (v) => /.+@.+\..+/.test(v) || "Emait n'est pas valide",
        ],
        lazy: false,
        snackbar: {
            enabled: false,
            text: '',
            color: ''
        }
    }),
    watch: {
        dialog(value) {
            if (!value) {
                this.pause();
            }
        },
    },
    methods: {
        async submit(){
            await this.user.post('/api/v1/token/login/')
            .then(response => {
                const token = response.data.auth_token

                this.$store.commit('setToken', token)

                axios.defaults.headers.common['Authorization'] = "Token " + token

                localStorage.setItem('token', token)

            })
            .catch(error => {
                if(error.response){
                    for (const property in error.response.data) {
                        this.snackbar.text += `${property}: ${error.response.data[property]}` + ','
                    }
                    this.snackbar.enabled = true
                    this.snackbar.color = "red"
                } else if (error.message) {
                    this.snackbar.text = 'Something went wrong. Please try again'
                    this.snackbar.enabled = true
                    this.snackbar.color = "red"

                    console.log(JSON.stringify(error))
                }
            })

            await axios.get('/api/v1/users/me/')
            .then(response =>{
                this.$store.commit('setUser', {'id': response.data.id, 'username': response.data.username})
                this.$router.push('/dashboard')
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        }
    },
};
</script>
