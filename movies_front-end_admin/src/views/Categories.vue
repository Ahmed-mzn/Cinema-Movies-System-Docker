<template>
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Categories</h1>
            </div>
        </div>

<div class="container"><br><br>
    <div class="box">
        <div class="column is-12 is-offset-10">
            <button @click="ShowAddModal()" class="button is-info"><span class="mr-1"><fa :icon="['fas', 'plus']"/></span> Add</button>
        </div>

        <div class="columns is-multiline">
            <div class="column is-10 is-offset-1">

                <table id="myTable" class="table is-fullwidth is-hoverable">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Name</th>
                            <th>Short decription</th>
                            <th>Created at</th>
                            <th>Action</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="category in categories"
                            :key="category.id"
                        >
                            <th>{{category.id}}</th>
                            <td>{{category.name}}</td>
                            <td>{{category.short_description}}</td>
                            <td>{{formatDate(category.created_at)}}</td>
                            <td>
                                <div class="buttons">
                                    <a @click="ShowDeleteModal(category.id)" class="button is-danger is-inverted"><span><fa :icon="['far', 'trash-alt']"/></span></a>
                                    <a @click="ShowEditModal(category)" class="button is-info is-inverted">
                                        <span><fa :icon="['far', 'edit']"/></span>
                                    </a>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>

            </div>
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
                                <input type="text" name="name" v-model="category.name" placeholder="Enter category name" class="input" :class="{ 'is-danger': category.errors.has('name') }">
                                <p 
                                    v-if="category.errors.has('name')"
                                    v-html="category.errors.get('name')"
                                    class="help is-danger"
                                >
                                </p>
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Short description</label>
                            <div class="control">
                                <textarea name="short_description" v-model="category.short_description" class="textarea" placeholder="Textarea" :class="{ 'is-danger': category.errors.has('short_description') }"></textarea>
                                <p 
                                    v-if="category.errors.has('short_description')"
                                    v-html="category.errors.get('short_description')"
                                    class="help is-danger"
                                >
                                </p>
                            </div>
                        </div>
                    </form>
                    
                </div>
            </div>
        </section>
        <footer class="modal-card-foot">
            <button v-if="!editMode" @click="addCategory" type="submit" class="button is-success">Add</button>
            <button v-if="editMode" @click="updateCategory" type="submit" class="button is-success">Save changes</button>

            <button @click="closeModal" class="button">Cancel</button>
        </footer>
        
    </div>
</div>

<!-- Delete Modal -->
<div class="modal" :class="showDeleteModal ? 'is-active' : ''">
    <div @click="closeModal" class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
            <p class="modal-card-title">Delete Category</p>
            <button @click="closeModal" class="delete" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <p>Are you sure ! you want too delete this workout ?</p>
                </div>
            </div>
        </section>
        <footer class="modal-card-foot">
            <button @click="deleteCategory" type="submit" class="button is-danger">Yes delete it</button>

            <button @click="closeModal" class="button">Cancel</button>
        </footer>
        
    </div>
</div>

</div><br><br><br><br>
</template>

<script>
import moment from 'moment'
import Form from 'vform'
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'Categories',
    data(){
        return {
            formValid: false,
            editMode: false,
            category: new Form({
                id: 0,
                name: '',
                short_description: '',

            }),
            showModal: false,
            showDeleteModal: false,
            categories: []
        }
    },
    mounted(){
        this.getCategories()
    },
    methods: {
        formatDate(date){
            return moment(date).locale('fr').format('LL')
        },
        async getCategories(){
            await axios.get('/api/v1/categories')
            .then(response =>{
                this.categories = response.data
                $(document).ready(function() {
                    $('#myTable').DataTable();
                } );
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        },
        addCategory(){
            this.category.errors.clear()
            if (this.category.name === '') {
                this.category.errors.set('name', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if (this.category.short_description === '') {
                this.category.errors.set('short_description', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if(this.formValid){
                const body = {
                    name: this.category.name,
                    short_description: this.category.short_description
                }
                axios.post('/api/v1/categories/', body)
                .then(response => {
                    toast({
                        message: 'The category was added',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right'
                    })
                    this.getCategories()
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
                this.category.reset()
            }
        },
        updateCategory(){
            this.category.clear()
            if (this.category.name === '') {
                this.category.errors.set('name', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if (this.category.short_description === '') {
                this.category.errors.set('short_description', 'This field may not be blank.')
                this.formValid = false
            } else {
                this.formValid = true
            }

            if(this.formValid){
                this.category.patch(`/api/v1/categories/${this.category.id}/`)
                .then(response => {
                    toast({
                        message: 'The category was updated',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right'
                    })
                    this.getCategories()
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
                this.category.reset()
            }
        },
        deleteCategory(){
            this.category.delete(`/api/v1/categories/${this.category.id}/`)
            .then(response => {
                toast({
                    message: 'The category was deleted',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right'
                })
                this.getCategories()
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
            this.category.reset()
        },
        ShowAddModal(){
            this.showModal = true
            this.editMode = false
            this.category.clear()
        },
        ShowDeleteModal(id){
            this.showDeleteModal = true
            this.category.id = id
        },
        closeModal(){
            this.showModal = false
            this.showDeleteModal = false
            this.category.reset()
            this.category.clear()
        },
        ShowEditModal(category){
            this.category.id = category.id
            this.category.name = category.name
            this.category.short_description = category.short_description
            this.showModal = true
            this.editMode = true
        }
        
    }
}
</script>

