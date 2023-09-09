<template>
  <div class="main-content has-background-sp">
    <div class="columns has-align-items-start is-mobile m-0">
      <div class="column is-full-mobile mx-0 px-0 pb-1">
        <div class="main-content p-2">
          <div class="columns has-align-items-stretch is-mobile mx-0 is-multiline is-overflow-auto has-invisible-scroll">
            <div
                class="column has-min-height-1 is-full-mobile is-one-third-tablet is-one-fifth-desktop is-one-fifth-fullhd is-one-fifth-widescreen is-wrap"
                v-for="user in users" :key="user.id">
              <div class="card main-content">
                <div class="card-image">
                  <figure class="image is-128x128 mx-auto">
                    <img class="is-rounded" v-if="user.photo.medium_square_crop" :src=user.photo.medium_square_crop alt="Placeholder image">
                    <img class="is-rounded" v-else src='../assets/no-no-user.jpg' alt="Placeholder image">
                  </figure>
                </div>
                <div class="card-content pt-4 pb-2 px-2 has-flex-1-0-auto">
                  <div class="media">
                    <div class="media-content has-text-centered">
                      <p class="title is-4" v-if="user.first_name">
                        {{ user.first_name }}
                        <span class="title is-4" v-if="user.last_name">
                          {{ user.last_name }}
                        </span>
                      </p>
                      <p class="title is-4" v-else>
                        Anonymous
                      </p>
                      <p class="subtitle is-6">@{{ user.username }}</p>
                    </div>
                  </div>

                  <div class="content">

                  </div>
                </div>
                <div class="card-footer">
                  <div class="card-footer-item">
                    <button type="button" @click="removeUser(user.id)" class="btn-grad-rude px-5" v-if="currentUser.following.includes(user.id)">
                      <font-awesome-icon icon="fa-solid fa-user-minus" />
                    </button>
                    <button type="button" @click="addUser(user.id)" class="btn-grad-lightblue px-5" v-else>
                      <font-awesome-icon icon="fa-solid fa-user-plus" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {toast} from "bulma-toast";
import axios from "axios";

export default {
  name: "UserSearch",
  data() {
    return {
      currentUser: [],
      users: [],
      query: '',
    }
  },
  beforeMount() {
    if (!this.$store.state.isAuthenticated) {
      this.$router.push('LogIn')
    }
  },
  async mounted() {
    document.title = 'search'
    let url = window.location.search.substring(1)
    let params = new URLSearchParams(url)
    if (params.get('query')) {
      this.query = params.get('query')
      await this.getCurrentUser()
      await this.performSearch()
    } else {
      toast({
        message: 'Please, Enter your queryset',
        type: "is-warning",
        position: "top-center",
        duration: 3000,
        pauseOnHover: true,
        dismissible: true,
      })

      this.$router.push('/')
    }

    document.title = `search '${this.query}'`
  },
  methods: {
    async performSearch() {
      await axios.post('http://127.0.0.1:8000/api/v1/account/users/search/', {'query': this.query})
          .then(response => {
            this.users = response.data
          })
          .catch(err => {
            toast({
              message: `Something going wrong: ${err}`,
              type: "is-warning",
              position: "top-center",
              duration: 2000,
              pauseOnHover: true,
              dismissible: true,
            })
          })
    },
    async getCurrentUser() {
      await axios.get(`http://127.0.0.1:8000/api/v1/account/${this.$store.state.username}/`)
          .then((response) => {
            this.currentUser = response.data
          })
          .catch((error) => {

            toast({
              message: `${error}`,
              type: "is-warning",
              position: "center",
              duration: 3000,
              pauseOnHover: true,
              dismissible: true,
            })
          })
    },
    async addUser(user_id) {
      await axios.post(`http://127.0.0.1:8000/api/v1/account/new-follow/`, {'following_id': user_id})
          .then((response) => {
            this.currentUser.following = response.data.following
          })
          .catch((error) => {
            console.log(error.data)
          })
    },
    async removeUser(user_id) {
      await axios.post(`http://127.0.0.1:8000/api/v1/account/unfollow/`, {'unfollow_id': user_id})
          .then((response) => {
            this.currentUser.following = response.data.following
          })
          .catch((error) => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>

</style>