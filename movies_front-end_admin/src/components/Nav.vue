<template>
    <nav class="navbar is-info" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <a href="/dashboard" class="navbar-item is-size-4"><span class="icon is-size-2 mr-4"><i class="fab fa-studiovinari"></i></span><b class="mr-2">CINEMA World</b> admin</a>
        </div>
    <template v-if="$store.state.user.isAuthenticated">
        <div class="navbar-menu" id="navbar-item">
            <div class="navbar-start">
                <router-link to="/dashboard" class="navbar-item"><span class="icon mr-1"><fa :icon="['fas', 'tachometer-alt']"/></span>Dashboard</router-link>
                <router-link to="/categories" class="navbar-item"><span class="icon mr-1"><fa :icon="['fas', 'cubes']"/></span>Categories</router-link>
                <router-link to="/movies" class="navbar-item"><span class="icon mr-1"><fa :icon="['fas', 'film']"/></span>Movies</router-link>
                <router-link to="/bookings" class="navbar-item"><span class="icon mr-1"><fa :icon="['fas', 'clipboard-list']"/></span>Bookings</router-link>
            </div>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    <button @click="logout" class="button is-danger"><span class="icon mr-1"><fa :icon="['fas', 'sign-out-alt']"/></span>Logout</button>
                </div>
            </div>
        </div>
    </template>
    </nav>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Nav',
    data(){
        return {
        }
    },
    methods: {
        logout() {
            axios.post('/api/v1/token/logout')
            .then(response => {

                axios.defaults.headers.common["Authorization"] = ""

                localStorage.removeItem("token")

                this.$store.commit('removeToken')

                this.$router.push('/log-in')
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
    }
}
</script>