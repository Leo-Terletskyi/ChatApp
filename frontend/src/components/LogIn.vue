<template>
  <div class="columns is-mobile is-centered">
    <div class="column is-four-fifths-mobile is-half-desktop">

      <div class="has-text-centered mb-4">
        <figure class="image is-192x192 is-inline-block">
          <img src="../assets/big-logo-no-background.svg" alt="">
        </figure>
      </div>

      <form @submit.prevent="LogInSubmit">
        <div class="field mb-4">
          <label class="label">Username</label>
          <div class="control">
            <input class="input" v-model="username" type="text" placeholder="">
          </div>
        </div>

        <div class="field mb-4">
          <label class="label">Password</label>
          <div class="control">
            <input class="input" v-model="password" type="password" placeholder="">
          </div>
        </div>

        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" :key="error">
            {{ error }}
          </p>
        </div>

        <button type="submit" class="btn-grad-lightgreen auth-form-btn-style mx-0 is-pulled-right">Submit</button>

      </form>

      <router-link to="/sign-up">
        <button type="button" class="btn-grad-lightblue auth-form-btn-style mx-0 is-pulled-left">
          New user? Register here.
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "LogIn",
  data() {
    return {
      username: '',
      email: '',
      password: '',
      errors: [],
    }
  },
  mounted() {
    document.title = 'Log in'
  },
  methods: {
    async LogInSubmit() {
      axios.defaults.headers.common['Authorization'] = ""
      localStorage.removeItem("token")

      this.errors = []
      if (this.username === '') {
        this.errors.push('The username is missing')
      }
      if (this.password === '') {
        this.errors.push('The password is missing')
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }
        console.log(formData)

        await axios
            .post('http://127.0.0.1:8000/api/v1/auth/token/login/', formData)
            .then(response => {
              const token = response.data.auth_token

              this.$store.commit('setToken', token)
              this.$store.commit('setUsername', formData.username)

              axios.defaults.headers.common['Authorization'] = "Token " + token

              toast({
                message: 'You have successfully logged in',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 1500,
                position: 'bottom-right'
              })

              setTimeout(() => {
                this.$router.push('/')
              }, 1500)

              this.$router.push('/')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else {
                this.errors.push('Something went wrong. Please try again')
                console.log(JSON.stringify(error))
              }
            })
      }
    }
  }
}
</script>

<style scoped>

</style>