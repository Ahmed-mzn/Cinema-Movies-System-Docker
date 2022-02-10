<template>
    <section id="hero">
        <v-parallax dark src="@/assets/img/about.jpg" height="750">
            <v-row align="center" justify="center">
                <v-col cols="10">
                    <v-row align="center" justify="center">
                        <v-col cols="12" md="6" xl="8">
                            <h1 class="display-2 font-weight-bold mb-4">Inscription</h1>
                            <h1 class="font-weight-light">
                                This registration able you to booking movies online <br />
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
                            <h1 class="display-2 font-weight-bold mb-4">Inscription</h1>
                            <v-form ref="form" v-model="valid" :lazy-validation="lazy">
                                <v-text-field
                                    v-model="user.first_name"
                                    :rules="nameRules"
                                    label="Nom"
                                    required
                                ></v-text-field>

                                <v-text-field
                                    v-model="user.last_name"
                                    :rules="nameRules"
                                    label="Prénom"
                                    required
                                ></v-text-field>

                                <v-text-field
                                    v-model="user.family_name"
                                    label="Nom du famille"
                                ></v-text-field>

                                <v-text-field
                                    v-model="user.password"
                                    :rules="nameRules"
                                    type="password"
                                    label="Mot de passe"
                                    required
                                ></v-text-field>

                                <v-text-field
                                    v-model="user.username"
                                    :rules="emailRules"
                                    label="E-mail"
                                    required
                                ></v-text-field>

                                <v-text-field
                                    v-model="user.phone_number"
                                    :rules="phoneRules"
                                    label="Numéro téléphone"
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
                                Envoyer
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
import Form from 'vform'
export default {
    data: () => ({
        user: new Form({
            username: "",
            first_name: "",
            last_name: "",
            password: '',
            family_name: "",
            phone_number: '',
            email: ''
        }),
        valid: true,
        phoneRules:[
            (v) => !!v || "Champ numéro téléphone est obligatoire",
        ],
        nameRules: [
            (v) => !!v || "Champ est obligatoire",
        ],
        emailRules: [
            (v) => !!v || "Champ email est obligatoire",
            (v) => /.+@.+\..+/.test(v) || "Emait n'est pas valide",
        ],
        textAreaRules: [
            (v) => !!v || "Champ message est obligatoire",
            (v) => (v && v.length >= 10) || "Au moins 10 caracters",
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
        submit(){
            this.user.email = this.user.username
            console.log(this.user)
            this.user.post("/api/v1/create_user")
            .then(response =>{
                console.log(response)
                this.snackbar.enabled = true
                this.snackbar.text = "Compte creer avec succès"
                this.snackbar.color = "success"
                this.$refs.form.reset()
                this.$router.push('/log-in')
            })
            .catch(error=> {
                for (const property in error.response.data) {
                    this.snackbar.text += `${property}: ${error.response.data[property]}` + ','
                }
                this.snackbar.enabled = true
                this.snackbar.color = "red"
                console.log(JSON.stringify(error))
            })
        }
    },
};
</script>
