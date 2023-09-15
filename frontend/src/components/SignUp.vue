<template>
  <div class="columns is-mobile is-centered">
    <div class="column is-four-fifths-mobile is-half-desktop">

      <div class="has-text-centered mb-4">
        <figure class="image is-192x192 is-inline-block">
          <img src="../assets/big-logo-no-background.svg" alt="">
        </figure>
      </div>

      <form @submit.prevent="signUpSubmit">
        <div class="field mb-4">
          <label class="label">Username</label>
          <div class="control">
            <input class="input" v-model="username" type="text" placeholder="e.g I_am_Groot">
          </div>
        </div>

        <div class="field mb-4">
          <label class="label">Email</label>
          <div class="control">
            <input class="input" v-model="email" type="email" placeholder="e.g. iamgroot@hokage.com">
          </div>
        </div>

        <div class="field mb-4">
          <label class="label">Password</label>
          <div class="control">
            <input class="input" v-model="password1" type="password" placeholder="e.g fjkdljo290f2j2fj029fjfeshdkjn,cm">
          </div>
        </div>

        <div class="field mb-4">
          <label class="label">Password confirm</label>
          <div class="control">
            <input class="input" v-model="password2" type="password" placeholder="">
          </div>
        </div>

        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" :key="error">
            {{ error }}
          </p>
        </div>

        <button type="submit" class="btn-grad-lightgreen auth-form-btn-style mx-0 is-pulled-right">Submit</button>

      </form>
      <router-link to="/login">
        <button type="button" class="btn-grad-lightblue auth-form-btn-style mx-0 is-pulled-left">
          Already have an account? Log in here.
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "SignUp",
  data() {
    return {
      username: '',
      email: '',
      password1: '',
      password2: '',
      errors: [],
    }
  },
  mounted() {
    document.title = 'Sign up'
  },
  methods: {
    async signUpRequest(formData) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/auth/users/', formData);

        toast({
          message: 'Account created, please log in',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 1500,
          position: 'bottom-right'
        })

        setTimeout(() => {
          this.$router.push('logIn')
        }, 1500)

      } catch (error) {
        console.log(error)
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }
          console.log(JSON.stringify(error.response.data))
        } else if (error.message) {
          this.errors.push('Something went wrong. Please try again')
          console.log(JSON.stringify(error))
        }
      }
    },

    signUpSubmit() {
      this.errors = []
      if (this.username === '') {
        this.errors.push('The username is missing')
      }
      if (this.password1 === '') {
        this.errors.push('The password is missing')
      }
      if (this.password1 !== this.password2) {
        this.errors.push('The passwords doesn\'t match')
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password1
        }

        this.signUpRequest(formData)
      }
    }
  }
}
</script>

<style scoped>

</style>