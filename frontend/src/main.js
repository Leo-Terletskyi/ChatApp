import {createApp} from 'vue'
import {createStore} from "vuex";
import axios from "axios";
import {createRouter, createWebHistory} from "vue-router";

import {library} from '@fortawesome/fontawesome-svg-core';
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';
import {faUser, faSearch} from '@fortawesome/free-solid-svg-icons'

library.add(faUser, faSearch)


import 'bulma/css/bulma.css'
import './style.css'
import App from './App.vue'
import Home from "./components/Home.vue";
import UserProfile from "./components/UserProfile.vue";
import SignUp from "./components/SignUp.vue";
import LogIn from "./components/LogIn.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/profile',
            name: 'profile',
            component: UserProfile
        },
        {
            path: '/sign-up',
            name: 'signUp',
            component: SignUp
        },
        {
            path: '/login',
            name: 'logIn',
            component: LogIn
        },
    ]
})

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token')
    // If logged in, or going to the Login page.
    if (token || to.name === 'logIn' || to.name === 'signUp') {
        // Continue to page.
        next()
    } else {
        // Not logged in, redirect to login.
        next({name: 'logIn'})
    }
})


const store = createStore({
    state: {
        isAuthenticated: false,
        token: '',
        username: 'anonymous',
    },
    getters: {
        get_user(state) {
            return state.username
        }
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
            if (localStorage.getItem('username')) {
                state.username = localStorage.getItem('username')
            } else {
                state.username = 'anonymous'
            }
        },
        setToken(state, token) {
            localStorage.setItem('token', token)
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state) {
            localStorage.setItem('token', '')
            state.token = ''
            state.isAuthenticated = false
        },
        setUsername(state, username) {
            localStorage.setItem('username', username)
            state.username = username
        },
        removeUsername(state) {
            localStorage.setItem('username', 'anonymous')
            state.username = 'anonymous'
        },
    },
    actions: {},
    modules: {}
})


const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(store)
app.use(router, axios)
app.mount('#app')
