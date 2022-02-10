<template>
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Movies</h1>
            </div>
        </div>

<div class="container"><br><br>

    <div class="column is-12 is-offset-11">
        <button @click="ShowAddModal()" class="button is-info"><span class="mr-1"><fa :icon="['fas', 'plus']"/></span> Add</button>
    </div>

    <div class="columns is-multiline">
        <div class="column is-12">

            <table id="myTable" class="table is-fullwidth is-hoverable">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Title</th>
                        <th>Category</th>
                        <th>Short decription</th>
                        <th>Hours</th>
                        <th>Image</th>
                        <th>Rating</th>
                        <th>Created At</th>
                        <th>Action</th>
                    </tr>
                </thead>

                <tbody>
                    <tr
                        v-for="movie in movies"
                        :key="movie.id"
                    >
                        <th>{{movie.id}}</th>
                        <td>{{movie.title}}</td>
                        <td>{{movie.category.name}}</td>
                        <td>{{movie.short_description}}</td>
                        <td>
                            <div class="tags">
                                <span v-for="hour in movie.hours" :key="hour" class="tag is-link is-light">{{hour.hour}}</span>
                            </div>
                        </td>
                        <td>
                            <figure class="image is-128x128">
                                <img :src="movie.get_image">
                            </figure>
                        </td>
                        <td>{{movie.rating}}<span class="ml-1 has-text-warning"><fa :icon="['fas', 'star']"/></span></td>
                        <td>{{formatDate(movie.date)}}</td>
                        <td>
                            <div class="buttons">
                                <a @click="ShowDeleteModal(movie.id)" class="button is-danger is-inverted"><span><fa :icon="['far', 'trash-alt']"/></span></a>
                                <a @click="ShowEditModal(movie)" class="button is-info is-inverted">
                                    <span><fa :icon="['far', 'edit']"/></span>
                                </a>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>

<!-- Ctg Modal -->
<div class="modal" :class="showModal ? 'is-active' : ''">
    <div @click="closeModal" class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
            <p class="modal-card-title">Category</p>
            <button @click="closeModal" class="delete" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
            <div class="columns">
                <div class="column is-12">
                    <form method="POST" action="">
                        <div class="field">
                            <label class="label">Name</label>
                            <div class="control">
                                <input type="text" name="title" v-model="movie.title" placeholder="Enter movie title" class="input" :class="{ 'is-danger': movie.errors.has('title') }">
                                <p 
                                    v-if="movie.errors.has('title')"
                                    v-html="movie.errors.get('title')"
                                    class="help is-danger"
                                >
                                </p>
                            </div>
                        </div>

                        <div class="field is-grouped">
                            <label class="label mr-3">Category</label>
                            <div class="control">
                                <div class="select">
                                    <select name="category" v-model="movie.category">
                                        <option value="0" selected>---Select Category---</option>
                                            <option 
                                                v-for="category in categories"
                                                :key="category.id"
                                                :value="category.id"
                                            >
                                                {{category.name}}
                                            </option>
                                    </select>
                                </div>
                            </div>
                            <label class="label mr-3">Rating</label>
                            <div class="control">
                                <div class="select">
                                    <select name="category" v-model="movie.rating">
                                            <option value="0" selected>---Select Rating---</option>
                                            <option value="1">Star</option>
                                            <option value="2">2 Stars</option>
                                            <option value="3">3 Stars</option>
                                            <option value="4">4 Stars</option>
                                            <option value="5">5 Stars</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Short description</label>
                            <div class="control">
                                <textarea name="short_description" v-model="movie.short_description" class="textarea" placeholder="Textarea" :class="{ 'is-danger': movie.errors.has('short_description') }"></textarea>
                                <p 
                                    v-if="movie.errors.has('short_description')"
                                    v-html="movie.errors.get('short_description')"
                                    class="help is-danger"
                                >
                                </p>
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Date</label>
                            <div class="control">
                                <input type="date" name="title" v-model="movie.date" placeholder="Enter movie title" class="input" :class="{ 'is-danger': movie.errors.has('title') }">
                                <p 
                                    v-if="movie.errors.has('date')"
                                    v-html="movie.errors.get('date')"
                                    class="help is-danger"
                                >
                                </p>
                            </div>
                        </div>

                        <div id="file-js" class="file has-name is-boxed">
                            <label class="file-label">
                                <input @change="fileChanged" id="file-input" class="file-input" type="file" accept="image/*" name="image">
                                <span class="file-cta">
                                    <span class="mr-1"><fa :icon="['fas', 'upload']"/></span>
                                    <span class="file-label">
                                        Choose a file…
                                    </span>
                                </span>
                                <span id="file-name" class="file-name"></span>
                            </label>
                        </div>
                        <label class="label mt-3">Hours</label>
                        <div class="field is-grouped is-grouped-multiline">
                            <p v-for="hour in hours" :key="hour" class="control">
                                <a @click="selectHour(hour.hour)" :class="movie.hours.includes(hour.hour) ? 'is-link' : '' " class="button">
                                    {{hour.hour}}
                                </a>
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </section>
        <footer class="modal-card-foot">
            <button v-if="!editMode" @click="addMovie" type="submit" class="button is-success">Add</button>
            <button v-if="editMode" @click="updateMovie" type="submit" class="button is-success">Save changes</button>

            <button @click="closeModal" class="button">Cancel</button>
        </footer>
        
    </div>
</div>

<!-- Delete Modal -->
<div class="modal" :class="showDeleteModal ? 'is-active' : ''">
    <div @click="closeModal" class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
            <p class="modal-card-title">Delete Movie</p>
            <button @click="closeModal" class="delete" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <p>Are you sure ! you want too delete this movie ?</p>
                </div>
            </div>
        </section>
        <footer class="modal-card-foot">
            <button @click="deleteMovie" type="submit" class="button is-danger">Yes delete it</button>

            <button @click="closeModal" class="button">Cancel</button>
        </footer>
        
    </div>
</div>

</div><br><br><br><br>
</template>

<script>
import Form from 'vform'

import axios from 'axios'
import moment from 'moment'
import { toast } from 'bulma-toast'
export default {
    name: 'Movies',
    data(){
        return {
            imgSelected: null,
            hours: [],
            categories: [],
            formValid: false,
            editMode: false,
            movie: new Form({
                id: 0,
                title: '',
                category: 0,
                short_description: '',
                rating: 0,
                hours: [],
                image: null,
                date: '',
                img_changed: 0

            }),
            showModal: false,
            showDeleteModal: false,
            movies: [],
        }
    },
    mounted(){
        this.getHours()
        this.getMovies()
        this.getCategories()
    },
    methods: {
        formatDate(date){
            return moment(date).locale('fr').format('LL')
        },
        async getHours(){
            await axios.get('/api/v1/get_hours')
            .then(response =>{
                this.hours = response.data
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        },
        async getMovies(){
            await axios.get('/api/v1/get_movies')
            .then(response =>{
                this.movies = response.data
                $(document).ready(function() {
                    $('#myTable').DataTable();
                } );
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        },
        async getCategories(){
            await axios.get('/api/v1/get_categories')
            .then(response =>{
                this.categories = response.data
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        },
        addMovie(){
            this.movie.clear()
            if (this.movie.title === '') {
                this.movie.errors.set('title', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if (this.movie.short_description === '') {
                this.movie.errors.set('short_description', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if(this.formValid){
                this.movie.image = this.imgSelected

                var hours = this.movie.hours

                this.movie.post('/api/v1/add_movie')
                .then(response => {
                    toast({
                        message: 'The movie was added',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right'
                    })
                    console.log(response.data.data.id)
                    const data = {
                        hours: hours,
                        movie: response.data.data.id
                    }
                    console.log(data)
                    axios.post('/api/v1/assigned_hours', data)
                    .then(response => {
                        console.log(response)
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                    this.getMovies()
                })
                .catch(error => {
                    toast({
                        message: 'Something went wrong. Please try again',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right'
                    })
                    console.log(JSON.stringify(error))
                })
                this.showModal = false
                this.movie.reset()
            }
        },
        updateMovie(){
            this.movie.clear()
            if (this.movie.title === '') {
                this.movie.errors.set('title', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if (this.movie.short_description === '') {
                this.movie.errors.set('short_description', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if(this.formValid){
                this.movie.image = this.imgSelected
                var hours = this.movie.hours
                console.log(this.movie.img_changed)
                this.movie.post(`/api/v1/update_movie/${this.movie.id}`)
                .then(response => {
                    const data = {
                        hours: hours,
                        movie: response.data.data.id
                    }
                    axios.post(`/api/v1/update_hours/${data.movie}`, data)
                    .then(response => {
                        toast({
                            message: 'The movie was updated',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })
                        this.getMovies()  
                    })
                    .catch(error => {
                        toast({
                            message: 'Something went wrong. Please try again',
                            type: 'is-danger',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })
                        console.log(JSON.stringify(error))
                    })
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                    toast({
                        message: 'Something went wrong. Please try again',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right'
                    })
                })
                this.showModal = false
                this.movie.reset()
            }
        },
        deleteMovie(){
            axios.delete(`/api/v1/movies/${this.movie.id}/`)
            .then(response => {
                toast({
                    message: 'The movie was deleted',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right'
                })
                this.getMovies()
            })
            .catch(error => {
                console.log(JSON.stringify(error))
                toast({
                    message: 'Something went wrong. Please try again',
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right'
                })
            })
            this.showDeleteModal = false
            this.movie.reset()
        },
        ShowAddModal(){
            this.showModal = true
            this.editMode = false
            this.movie.clear()
        },
        ShowDeleteModal(id){
            this.showDeleteModal = true
            this.movie.id = id
        },
        closeModal(){
            this.showModal = false
            this.showDeleteModal = false
            this.movie.reset()
            this.movie.clear()
        },
        ShowEditModal(movie){
            this.movie.id = movie.id
            this.movie.title = movie.title
            this.movie.date = movie.date
            this.movie.category = movie.category.id
            for(let i=0; i< movie.hours.length; i++){
                this.movie.hours.push(movie.hours[i].hour)
            }
            this.movie.rating = movie.rating
            this.movie.short_description = movie.short_description
            $('#file-input').attr("src", movie.get_image);
            this.showModal = true
            this.editMode = true
        },
        selectHour(hour){
            var check = 0
            for(let i=0; i< this.movie.hours.length; i++){
                if(this.movie.hours[i].hour == hour){
                    check = 1
                }
            }
            if(check){
                const index = this.movie.hours.indexOf(hour);
                this.movie.hours.splice(index, 1);
            } else{
                this.movie.hours.push(hour)
            }
        },
        getClass(hour){
            for(let i=0; i< this.movie.hours.length; i++){
                if(this.movie.hours[i].id == hour.id){
                    return true;
                } else {
                    return false;
                }
            }
        },
        fileChanged(event){
            this.imgSelected = event.target.files[0]
            $('#file-name').text(event.target.files[0].name);
            this.movie.img_changed = 1
            this.movie.image = this.imgSelected
            // console.log(this.imgSelected)
        }
    },
}
</script>