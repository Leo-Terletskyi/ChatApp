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
    </div>
  </div>
</template>

<script>
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
        console.log(formData)

        this.$router.push('/log-in')
      }
    }
  }
}
</script>

<style scoped>

</style>