<template>
  <div>
    <v-navigation-drawer
      v-model="drawer"
      app
      temporary
      dark
      src="@/assets/img/bgDrawer.jpg"
    >
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <img src="@/assets/img/logo.png" alt="Logo" />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="title">Calango</v-list-item-title>
            <v-list-item-subtitle>WEB</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider />

      <v-list dense>
        <v-list-item
          v-for="([icon, text, link], i) in items"
          :key="i"
          link
          @click="$router.push(link)"
        >
          <v-list-item-icon class="justify-center">
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="subtitile-1">{{
              text
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      :color="color"
      :flat="flat"
      dark
      class="px-15"
      :class="{ expand: flat }"
    >
      <v-toolbar-title>
        <v-img src="@/assets/img/logo.png" max-width="50px" />
      </v-toolbar-title>
      <v-spacer />
      <v-app-bar-nav-icon
        @click.stop="drawer = !drawer"
        class="mr-4"
        v-if="isXs"
      />
      <div v-else>
        <v-btn text to="/">
          <span class="mr-2">Home</span>
        </v-btn>
        <v-btn text to="/movies">
          <span class="mr-2">Movies</span>
        </v-btn>
        <v-btn text to="/about-us">
          <span class="mr-2">About us</span>
        </v-btn>
        <template v-if="currentRouteName == 'Home'">
          <v-btn text @click="$vuetify.goTo('#pricing')">
            <span class="mr-2">Plans</span>
          </v-btn>
          <v-btn text @click="$vuetify.goTo('#contact')">
            <span class="mr-2">Contactez-nous</span>
          </v-btn>
        </template>
        <template v-if="!$store.state.user.isAuthenticated">
          <v-btn rounded outlined text to="log-in">
            <span class="mr-3">Connecter</span>
          </v-btn>
          <v-btn class="ml-5" rounded outlined text to="sign-up">
            <span class="mr-3">Inscription</span>
          </v-btn>
        </template>
        <template v-else>
          <v-btn text to="/dashboard">
            <span class="mr-2">Dashboard</span>
          </v-btn>
          <v-btn @click="logout" color="red" text>
            <span class="mr-2">Logout</span><v-icon>mdi-logout</v-icon>
          </v-btn>
        </template>
      </div>
    </v-app-bar>
  </div>
</template>

<style scoped>
.v-toolbar {
  transition: 0.6s;
}

.expand {
  height: 80px !important;
  padding-top: 10px;
}
</style>

<script>
import axios from 'axios'
export default {
  data: () => ({
    drawer: null,
    isXs: false,
    items: [
      ["mdi-home-outline", "Home", "/"],
      ["mdi-information-outline", "Movies", "/movies"],
      ["mdi-download-box-outline", "About us", "#aboutus"],
      ["mdi-download-box-outline", "Plans", "#pricing"],
      ["mdi-email-outline", "Contactez-Nous", "#contact"],
    ],
  }),
  props: {
    color: String,
    flat: Boolean,
  },
  methods: {
    onResize() {
      this.isXs = window.innerWidth < 850;
    },
    logout(){
      axios.post('/api/v1/token/logout')
      .then(() => {

        axios.defaults.headers.common["Authorization"] = ""

        localStorage.removeItem("token")

        this.$store.commit('removeToken')

        this.$router.push('/')
      })
      .catch(error => {
        if (error.response) {
            console.log(JSON.stringify(error.response.data))
        } else if(error.message) {
            console.log(JSON.stringify(error.message))
        } else {
            console.log(JSON.stringify(error))
        }
      })
    }
  },

  watch: {
    isXs(value) {
      if (!value) {
        if (this.drawer) {
          this.drawer = false;
        }
      }
    },
  },
  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
  },
  computed: {
      currentRouteName() {
          return this.$route.name;
      }
  }
};
</script>
