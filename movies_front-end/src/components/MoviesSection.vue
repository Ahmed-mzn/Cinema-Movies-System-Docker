<template>
  <section id="hero">
    <v-parallax dark src="@/assets/img/test4.jpg" height="750">
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <v-col cols="12" md="6" xl="8">
              <h1 class="display-2 font-weight-bold mb-4">Movies</h1>
              <h1 class="font-weight-light">
                Lorem ipsum dolor sit amet consectetur <br />
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
      <!-- iterator -->
      <v-container fluid>
        <v-data-iterator
          :items="movies"
          :items-per-page.sync="itemsPerPage"
          :page.sync="page"
          :search="search"
          :sort-by="sortBy.toLowerCase()"
          :sort-desc="sortDesc"
          hide-default-footer
        >
          <template v-slot:header>
            <v-toolbar
              dark
              rounded
              color="blue darken-3"
              class="mb-1"
            >
              <v-text-field
                v-model="search"
                clearable
                flat
                solo-inverted
                hide-details
                prepend-inner-icon="mdi-magnify"
                label="Search"
              ></v-text-field>
              <template v-if="$vuetify.breakpoint.mdAndUp">
                <v-spacer></v-spacer>
                <v-select
                  v-model="sortBy"
                  flat
                  solo-inverted
                  hide-details
                  :items="keys"
                  prepend-inner-icon="mdi-magnify"
                  label="Sort by"
                ></v-select>
                <v-spacer></v-spacer>
                <v-btn-toggle
                  v-model="sortDesc"
                  mandatory
                >
                  <v-btn
                    large
                    depressed
                    color="blue"
                    :value="false"
                  >
                    <v-icon>mdi-arrow-up</v-icon>
                  </v-btn>
                  <v-btn
                    large
                    depressed
                    color="blue"
                    :value="true"
                  >
                    <v-icon>mdi-arrow-down</v-icon>
                  </v-btn>
                </v-btn-toggle>
              </template>
            </v-toolbar>
          </template>

          <template v-slot:default="props">
            <v-row align="center" justify="center">
              <v-col cols="10">
                <v-row align="center" justify="space-around">
                  <v-col
                    cols="12"
                    sm="4"
                    class="text-center"
                    v-for="movie in props.items"
                    :key="movie.id"
                  >
                    <v-hover v-slot:default="{ hover }">
                      <v-card 
                        class="mx-auto my-12" 
                        max-width="374"
                        :elevation="hover ? 10 : 4"
                        :class="{ up: hover }"
                      >
                        <template slot="progress">
                          <v-progress-linear
                            color="deep-purple"
                            height="10"
                            indeterminate
                          ></v-progress-linear>
                        </template>

                        <v-img @click="movieDetails(movie)" height="250" :src="movie.get_image"></v-img>

                        <v-card-title @click="movieDetails(movie)">{{ movie.title }}</v-card-title>

                        <v-card-text>
                          <v-row align="center" class="mx-0">
                            <v-rating
                              :value="movie.rating"
                              color="amber"
                              dense
                              half-increments
                              readonly
                              size="14"
                            ></v-rating>

                            <div class="grey--text ms-4">
                              {{ movie.rating }}
                            </div>
                          </v-row>
                          <v-row align="center" class="mx-0">
                            <div class="my-3 text-subtitle-1">
                              <b>{{movie.category}}</b>
                            </div>
                          </v-row>

                          <div>{{ movie.short_description }}</div>

                          <v-row align="center" class="mx-0">
                            <div class="mt-5">
                              <b>{{movie.date}}</b>
                            </div>
                          </v-row>
                        </v-card-text>
                        <v-divider class="mx-4"></v-divider>

                        <v-card-title>Les heurs Disponible</v-card-title>

                        <v-card-text>
                          <v-chip-group
                            active-class="deep-purple accent-4 white--text"
                            column
                          >
                            <v-chip v-for="hour in movie.hours" :key="hour.id">{{
                              hour.hour
                            }}</v-chip>
                          </v-chip-group>
                        </v-card-text>

                        <v-card-actions>
                          <v-btn color="deep-purple lighten-2" text @click="formReserve(movie)">
                            Reserve
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-hover>
                  </v-col>
                </v-row>
                <div class="text-center">
                </div>
              </v-col>
            </v-row>
          </template>
          <template v-slot:footer>
            <v-row
              class="mt-2"
              align="center"
              justify="center"
            >
              <span class="grey--text">Items per page</span>
              <v-menu offset-y>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    dark
                    text
                    color="primary"
                    class="ml-2"
                    v-bind="attrs"
                    v-on="on"
                  >
                    {{ itemsPerPage }}
                    <v-icon>mdi-chevron-down</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                    v-for="(number, index) in itemsPerPageArray"
                    :key="index"
                    @click="updateItemsPerPage(number)"
                  >
                    <v-list-item-title>{{ number }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>

              <v-spacer></v-spacer>

              <span
                class="mr-4
                grey--text"
              >
                Page {{ page }} of {{ numberOfPages }}
              </span>
              <v-btn
                fab
                dark
                color="blue darken-3"
                class="mr-1"
                @click="formerPage"
              >
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
              <v-btn
                fab
                dark
                color="blue darken-3"
                class="ml-1"
                @click="nextPage"
              >
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-row>
          </template>
        </v-data-iterator>
      </v-container>
      <v-spacer></v-spacer>
      <br>
      <!-- end iterator -->
      <v-row justify="center">
        <v-dialog
          v-model="dialog"
          persistent
          max-width="600px"
        >
          <v-form 
            ref="form"
            v-model="valid"
            lazy-validation
          >
            <v-card>
              <v-card-title>
                <span class="text-h5">Saisie vos informations</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <template v-if="!$store.state.user.isAuthenticated">
                      <v-col
                        cols="12"
                        sm="6"
                        md="4"
                      >
                        <v-text-field
                          label="Nom*"
                          required
                          hint="Entrer ici votre nom"
                          :rules="[v => !!v || 'Nom is required']"
                          v-model="booking.first_name"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="4"
                      >
                        <v-text-field
                          label="Prénom*"
                          hint="Entrer ici votre pénom"
                          :rules="[v => !!v || 'Prenom is required']"
                          v-model="booking.last_name"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="4"
                      >
                        <v-text-field
                          label="Nom de famille"
                          hint="Entrer ici votre nom de famille"
                          persistent-hint
                          v-model="booking.family_name"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          label="Email*"
                          required
                          :rules="[v => !!v || 'E-mail is required', v => /.+@.+/.test(v) || 'E-mail must be valid',]"
                          v-model="booking.email"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          label="Numero téléphone*"
                          required
                          :rules="[v => !!v || 'Telephone is required']"
                          v-model="booking.phone_number"
                        ></v-text-field>
                      </v-col>
                    </template>
                    <v-col
                      cols="12"
                      sm="6"
                    >
                      <v-select
                        :items="['cash', 'online', ]"
                        label="Type de payment*"
                        hint="Choisir mode de paiement preferer"
                        required
                        :rules="[v => !!v || 'Payment type is required']"
                        v-model="booking.payment_type"
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-container>
                <small>*Champ obligatoire</small>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog = false"
                >
                  Annuler
                </v-btn>
                <v-btn
                  v-if="booking.payment_type=='online'"
                  color="blue darken-1"
                  text
                  @click="validate"
                  :disabled="!valid"
                >
                  Proceder au payment
                </v-btn>
                <v-btn
                  v-else
                  color="blue darken-1"
                  text
                  @click="validate"
                  :disabled="!valid"
                >
                  Reserver
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-form>
        </v-dialog>
      </v-row>
    </v-container>
    <div class="svg-border-waves">
      <img src="~@/assets/img/wave2.svg" />
    </div>
    <v-snackbar
        v-model="snackbar.enabled"
        timeout="3000"
        right
        top
        :color="snackbar.color"
    >
      {{ snackbar.text }}

      <template v-slot:action="{ attrs }">
        <v-btn
            text
            v-bind="attrs"
            @click="snackbar.enabled = false"
        >
          close
        </v-btn>
      </template>
    </v-snackbar>
    <v-snackbar
      v-model="snackbar2"
      color="success"
      timeout="3000"
    >
      Reservation est faite avec succès

      <template v-slot:action="{ attrs }">
        <v-btn
          color="pink"
          text
          v-bind="attrs"
          @click="snackbar2 = false"
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
import { toast } from 'bulma-toast'
export default {
  data() {
    return {
      itemsPerPageArray: [6, 9, 12],
      search: '',
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 6,
      sortBy: 'name',
      keys: [
        'Title',
        'Rating',
        'Category',
        'Date',
        'Hours'
      ],
      booking: new Form({
        user: 0,
        movie: 0,
        first_name: '',
        last_name: '',
        family_name: '',
        email: '',
        phone_number: '',
        payment_type: '',
        payed: false
      }),
      valid: false,
      dialog: false,
      movies: [],
      snackbar2: false,
      snackbar: {
        enabled: false,
        text: '',
        color: ''
      }
    };
  },
  mounted(){
    this.getMovies()
  },
  methods: {
    async getMovies(){
      await axios.get('/api/v1/get_movies')
      .then(response =>{
        this.movies = response.data
        for(let i=0; i<this.movies.length; i++){
          this.movies[i].category = this.movies[i].category.name
        }
      })
      .catch(error =>{
        console.log(JSON.stringify(error))
      })
    },
    validate () {
      this.$refs.form.validate()
      if(this.$store.state.user.isAuthenticated){
        this.booking.user = this.$store.state.user.id
        this.booking.post('/api/v1/add_booking')
          .then((response) => {
            this.snackbar.text = "Reservation est faite avec succès"
            this.snackbar.color = "success"
            this.snackbar.enabled = true
            this.snackbar2 = true
            toast({
                message: 'Reservation est faite avec succès',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right'
            })
            this.$router.push('/payment/'+response.data.id)
          })
          .catch(error => {
            this.snackbar.text = "Something went wrong. Please try again"
            this.snackbar.color = "red"
            this.snackbar.enabled = true
            this.snackbar2 = true
            console.log(JSON.stringify(error))
          })
        this.dialog = false
        this.$refs.form.resetValidation()
        this.booking.reset()
      } else {
        if(this.$refs.form.validate()){
          this.booking.post('/api/v1/add_booking')
            .then((response) => {
              this.snackbar.text = "Reservation est faite avec succès"
              this.snackbar.color = "success"
              this.snackbar.enabled = true
              this.$router.push('/payment/'+response.data.id)
            })
            .catch(error => {
              this.snackbar.text = "Something went wrong. Please try again"
              this.snackbar.color = "red"
              this.snackbar.enabled = true
              console.log(JSON.stringify(error))
            })
          this.dialog = false
          this.$refs.form.resetValidation()
          this.booking.reset()
        }
      }
    },
    formReserve(movie){
      this.booking.reset()
      this.dialog = true
      this.booking.movie = movie.id
    },
    nextPage () {
      if (this.page + 1 <= this.numberOfPages) this.page += 1
    },
    formerPage () {
      if (this.page - 1 >= 1) this.page -= 1
    },
    updateItemsPerPage (number) {
      this.itemsPerPage = number
    },
    movieDetails(movie){
      console.log(movie.id)
    },
  },
  computed: {
    numberOfPages () {
      return Math.ceil(this.movies.length / this.itemsPerPage)
    },
    filteredKeys () {
      return this.keys.filter(key => key !== 'Name')
    },
  },
};
</script>
