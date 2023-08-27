<template>
  <div class="main-content has-background-sp">
    <div class="columns is-mobile is-centered m-0">
      <div class="column is-full-mobile is-half-desktop is-half-fullhd is-half-widescreen is-two-thirds-tablet">
        <div class="main-content">
          <div class="card-header gradient-box">
            <div class="gradient-overlay">
              <p class="card-header-title has-text-white is-centered">
                Profile
              </p>
            </div>
            <span class="card-header-title has-text-white is-centered">
              Profile
            </span>
          </div>
          <div class="card main-card flex-body">
            <div class="card-content main-card flex-body main-content has-height-100 p-2">
              <figure class="image is-128x128">
                <img src="https://bulma.io/images/placeholders/128x128.png">
              </figure>

              <div class="field my-2">
                <label class="label">Username cannot be changed</label>
                <div class="control">
                  <input class="input" disabled type="text" placeholder="Username">
                </div>
              </div>

              <form @submit.prevent>
                <div class="field my-4">
                  <label class="label">Email</label>
                  <div class="control">
                    <input class="input" type="email" placeholder="change your email">
                  </div>
                </div>

                <label class="label">Photo</label>
                <div class="file has-name mb-4">
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
export default {
  name: "UserProfile",
  data() {
    return {
      email: '',
      photo: '',
      photoName: ''
    }
  },
  beforeMount() {
    if (!this.$store.state.isAuthenticated) {
      this.$router.push('/log-in')
    }
    document.title = 'My Profile'
  },
  methods: {
    onPhotoChange(event) {
      const fileData = event.target.files[0];
      this.photoName = fileData.name
      this.photo = fileData
      console.log(this.photo)
    }
  }
}
</script>

<style scoped>

</style>