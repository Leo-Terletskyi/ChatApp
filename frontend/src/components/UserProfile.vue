<template>
  <div class="main-content has-background-sp">
    <div class="columns is-mobile is-centered m-0">
      <div class="column is-full-mobile is-half-desktop is-half-fullhd is-half-widescreen is-two-thirds-tablet">
        <div class="main-content">
          <div class="card-header gradient-box has-fz-20">
            <div class="gradient-overlay">
              <p class="card-header-title has-text-white is-centered">
                Profile: <span class="has-text-lightskyblue has-shadow-darkgray mx-2">{{ getUsername }}</span>
              </p>
            </div>
            <span class="card-header-title has-text-white is-centered">
              Profile: <span class="has-text-darkorange has-shadow-darkgray mx-2">{{ getUsername }}</span>
            </span>
          </div>
          <div class="card main-card flex-body">
            <div class="card-content main-card flex-body main-content has-height-100 p-2">
              <figure class="image is-128x128" v-if=user.photo>
                <img :src=user.photo alt="">
              </figure>

              <figure class="image is-128x128" v-else>
                <img src="../assets/no-no-user.jpg" alt="">
              </figure>

              <div class="field mt-5 mb-2">
                <label class="label">Username cannot be changed</label>
                <div class="control">
                  <input class="input" disabled type="text" :placeholder=getUsername>
                </div>
              </div>

              <form @submit.prevent="updateProfile">
                <div class="field my-5">
                  <label class="label">First name</label>
                  <div class="control">
                    <input class="input" type="text" :placeholder=user.first_name  v-model="formData.first_name">
                  </div>
                </div>

                <div class="field my-5">
                  <label class="label">Last name</label>
                  <div class="control">
                    <input class="input" type="text" :placeholder=user.last_name  v-model="formData.last_name">
                  </div>
                </div>

                <div class="field my-5">
                  <label class="label">Email</label>
                  <div class="control">
                    <input class="input" type="email" :placeholder=user.email  v-model="formData.email">
                  </div>
                </div>

                <label class="label">Photo</label>
                <div class="file has-name mb-5">
                  <label class="file-label">
                    <input class="file-input" type="file" name="photo" @change="onPhotoChange">
                    <span class="file-cta">
                      <span class="file-icon">
                        <i class="fas fa-upload"></i>
                      </span>
                      <span class="file-label">
                        Choose a file…
                      </span>
                    </span>
                    <span class="file-name">
                      {{ photoName }}
                    </span>
                  </label>
                </div>

                <div class="field my-5">
                  <label class="label">Phone</label>
                  <div class="control">
                    <input class="input" type="tel" :placeholder=user.phone v-model="formData.phone">
                  </div>
                </div>

                <div class="field my-5" v-if="!user.birthday">
                  <label class="label">Birthday</label>
                  <div class="control">
                    <input class="input" type="date" v-model="formData.birthday">
                  </div>
                </div>

                <div class="field my-5" v-else>
                  <label class="label">Birthday "this field is already filled"</label>
                  <div class="control">
                    <input class="input" disabled type="text" :placeholder=user.birthday>
                  </div>
                </div>


                <button type="submit" class="btn-grad-lightgreen auth-form-btn-style mx-0 is-pulled-right">Submit</button>
              </form>
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
  name: "UserProfile",
  data() {
    return {
      user: [],
      formData: {
        first_name: '',
        last_name: '',
        email: '',
        photo: null,
        birthday: '',
        phone: '',
      },
      photoName: '',
    }
  },
  beforeMount() {
    if (!this.$store.state.isAuthenticated) {
      this.$router.push('/log-in')
    }
    document.title = 'My Profile'
  },
  async mounted() {
    await this.getUser()
  },
  computed: {
    getUsername() {
      return this.$store.state.username
    },
  },

  methods: {
    async getUser() {
      await axios.get(`http://127.0.0.1:8000/api/v1/account/${this.getUsername}/`)
          .then((response) => {
            this.user = response.data
            this.user.photo = response.data.photo.medium_square_crop
          })
          .catch((err) => {
            console.log(err)
          })
    },

    onPhotoChange(event) {
      const fileData = event.target.files[0];
      this.photoName = fileData.name
      this.formData.photo = fileData
    },
    async updateProfile() {
      const formData = new FormData()

      if (this.formData.first_name) {
        formData.append('first_name', this.formData.first_name);
      }
      if (this.formData.last_name) {
        formData.append('last_name', this.formData.last_name);
      }
      if (this.formData.email) {
        formData.append('email', this.formData.email);
      }
      if (this.formData.birthday) {
        formData.append('birthday', this.formData.birthday);
      }
      if (this.formData.phone) {
        formData.append('phone', this.formData.phone);
      }
      if (this.formData.photo) {
        formData.append('photo', this.formData.photo);
      }

      await axios.patch(`http://127.0.0.1:8000/api/v1/account/${this.getUsername}/`, formData, {
        headers: {'Content-Type': 'multipart/form-data'}
      })
          .then(() => {
            this.formData.first_name = ''
            this.formData.last_name = ''
            this.formData.email = ''
            this.formData.photo = null
            this.formData.birthday = ''
            this.formData.phone = ''
            this.getUser()
          })
          .catch((err) => {
            console.log(err)
          })
    },
  }
}
</script>

<style scoped>

</style>