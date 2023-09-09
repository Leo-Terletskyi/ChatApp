<template>
  <div class="main-content has-background-sp">
    <div class="columns is-mobile m-0">
      <div class="column is-half">
        <div class="main-content">
          <div class="card-header has-background-fresh-oasis">
            <p class="card-header-title has-text-white">
              Contacts
            </p>
          </div>
          <div class="card main-card flex-body has-invisible-scroll">
            <div class="card-content main-card main-content flex-body has-height-100 p-2">
              <div v-for="user in contacts" :key="user.id">
                <div class="box p-1 my-2">
                  <article class="media">
                    <div class="media-left">
                      <figure class="image is-32x32">
                        <img v-if="user.photo.small_square_crop" :src=user.photo.small_square_crop alt="Image">
                        <img v-else src="../assets/no-no-user.jpg" alt="Image">
                      </figure>
                    </div>
                    <div class="media-content pt-1">
                      <div class="content">
                        <p>
                          <strong>@{{ user.username }}</strong> <small></small>
                          <button @click="removeUser(user.id)" type="button" class="btn-grad-rude px-5 is-pulled-right m-0">
                            <font-awesome-icon icon="fa-solid fa-user-minus"/>
                          </button>
                        </p>
                      </div>
                    </div>
                  </article>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="column is-half">
        <div class="main-content">
          <div class="card-header has-background-phoenix-start">
            <p class="card-header-title has-text-white">
              Followers
            </p>
          </div>
          <div class="card main-card flex-body has-invisible-scroll">
            <div class="card-content main-card flex-body main-content has-height-100 p-2">
              <div v-for="user in followers" :key="user.id">
                <div class="box p-1 my-2">
                  <article class="media">
                    <div class="media-left">
                      <figure class="image is-32x32">
                        <img v-if="user.photo.small_square_crop" :src="user.photo.small_square_crop" alt="Image">
                        <img v-else src="../assets/no-no-user.jpg" alt="Image">
                      </figure>
                    </div>
                    <div class="media-content pt-1">
                      <div class="content">
                        <p>
                          <strong>@{{ user.username }}</strong> <small></small>
                          <button @click="addUser(user.id)" type="button" class="btn-grad-lightgreen px-5 is-pulled-right m-0">
                            <font-awesome-icon icon="fa-solid fa-user-plus"/>
                          </button>
                        </p>
                      </div>
                    </div>
                  </article>
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
import axios from "axios";

export default {
  name: "ContactManagement",
  data() {
    return {
      currentUser: [],
      contacts: [],
      followers: []
    }
  },
  beforeMount() {
    if (!this.$store.state.isAuthenticated) {
      this.$router.push('LogIn')
    }
  },
  async mounted() {
    document.title = 'contact-management'
    await this.getCurrentUser()
    await this.getContacts()
  },
  methods: {
    async getCurrentUser() {
      await axios.get(`http://127.0.0.1:8000/api/v1/account/${this.$store.state.username}/`)
          .then((response) => {
            this.currentUser = response.data
          })
          .catch((error) => {
            console.log(error)
          })
    },
    async getContacts() {
      await axios.get('http://127.0.0.1:8000/api/v1/account/contact-management/')
          .then((response) => {
            response.data.forEach((user) => {
              if (this.currentUser.following.includes(user.id)) {
                this.contacts.push(user)
              } else {
                this.followers.push(user)
              }
            })
          })
          .catch((error) => {
            console.log(error)
          })
    },
    async addUser(user_id) {
      await axios.post(`http://127.0.0.1:8000/api/v1/account/new-follow/`, {'following_id': user_id})
          .then((response) => {
            this.currentUser.following = response.data.following

            this.followers = this.followers.filter(user => {
              if (user.id===user_id) {
                this.contacts.push(user)
                return false
              }
              return true
            })
          })
          .catch((error) => {
            console.log(error.data)
          })
    },
    async removeUser(user_id) {
      await axios.post(`http://127.0.0.1:8000/api/v1/account/unfollow/`, {'unfollow_id': user_id})
          .then((response) => {
            this.currentUser.following = response.data.following

            this.contacts = this.contacts.filter(user => {
              if (user.id===user_id) {
                this.followers.push(user)
                return false
              }
              return true
            })

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