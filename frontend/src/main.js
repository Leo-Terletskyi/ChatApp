import {createApp} from 'vue'
import {createStore} from "vuex";

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
            path: '/log-in',
            name: 'logIn',
            component: LogIn
        },
    ]
})


const store = createStore({
    state() {
        return {
            isAuthenticated: true,
            username: '',
            token: '',

        }
    },
    mutations: {}
})


const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(store)
app.use(router)
app.mount('#app')
