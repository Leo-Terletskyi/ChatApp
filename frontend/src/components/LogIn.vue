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
          <label class="label">Email</label>
          <div class="control">
            <input class="input" v-model="email" type="email" placeholder="">
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
    </div>
  </div>
</template>

<script>
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
    document.title = 'Sign up'
  },
  methods: {
    LogInSubmit() {
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

        this.$router.push('/')
      }
    }
  }
}
</script>

<style scoped>

</style>