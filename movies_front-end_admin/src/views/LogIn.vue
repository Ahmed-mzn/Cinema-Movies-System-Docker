<template>
    <div class="login">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Log in</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-8 is-offset-2">
                        <div class="box">
                            <form @submit.prevent="submitForm">
                                <div class="field">
                                    <label class="label">Username</label>
                                    <div class="control">
                                        <input type="text" placeholder="Enter email" class="input" v-model="user.username" :class="{ 'is-danger': user.errors.has('username') }">
                                        <p 
                                            v-if="user.errors.has('username')"
                                            v-html="user.errors.get('username')"
                                            class="help is-danger"
                                        >
                                        </p>
                                    </div>
                                </div>

                                <div class="field">
                                    <label class="label">Password</label>
                                    <div class="control">
                                        <input type="password" placeholder="Enter password" class="input" v-model="user.password" :class="{ 'is-danger': user.errors.has('password') }">
                                        <p 
                                            v-if="user.errors.has('password')"
                                            v-html="user.errors.get('password')"
                                            class="help is-danger"
                                        >
                                        </p>
                                    </div>
                                </div>

                                <template v-if="errors.length">
                                    <article 
                                        class="message is-danger mt-5"  
                                        v-for="error in errors"
                                        :key="error"
                                    >
                                        <div class="message-body">
                                            {{ error }}
                                        </div>
                                    </article>
                                </template>

                                <div class="field">
                                    <div class="control">
                                        <button class="button is-info">Log in</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>


<script>
import Form from 'vform'
import axios from 'axios'

export default {
    name: 'SignUp',
    data() {
        return {
            user: new Form({
                username: '',
                password: '',
            }),
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.user.errors.clear()

            if (this.user.username === '') {
                this.errors.push('This username may not be blank.')
                this.user.errors.set('username', 'This field may not be blank.')
            }

            if (this.user.password === '') {
                this.errors.push('This password may not be blank.')
                this.user.errors.set('password', 'This field may not be blank.')
            }

            if(!this.errors.length){

                this.user.post('/api/v1/token/login/')
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common['Authorization'] = "Token " + token

                    localStorage.setItem('token', token)


                    window.location.href = '/dashboard'
                })
                .catch(error => {
                    if(error.response){
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else if (error.message) {
                        this.errors.push('Something went wrong. Please try again')

                        console.log(JSON.stringify(error))
                    }
                })
            }
        }
    }
}
</script>
