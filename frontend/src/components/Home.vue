<template>
  <div class="main-content has-background-sp">
    <div class="columns is-mobile m-0">
      <div class="column is-two-fifths-mobile is-two-fifths-tablet is-one-fifth-desktop is-one-fifth-fullhd is-one-fifth-widescreen">
        <div class="main-content">
          <div class="card-header has-background-fresh-oasis">
            <p class="card-header-title has-text-white">
              Contacts
            </p>
          </div>
          <div class="card main-card flex-body">
            <div class="card-content main-card main-content flex-body has-height-100 p-2">
              <div v-for="friend in friends" :key="friend.id">
                <div class="box p-1 my-2">
                  <article class="media">
                    <div class="media-left">
                      <figure class="image is-32x32">
                        <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
                      </figure>
                    </div>
                    <div class="media-content">
                      <div class="content">
                        <p>
                          <strong>John Smith</strong> <small>@johnsmith</small> <span class="tag is-success is-pulled-right">Online</span>
                        </p>
                      </div>
                    </div>
                  </article>
                </div>
              </div>
            </div>
            <div class="card-footer">
              <div class="card-footer-item">
                <form @submit.prevent="sendMessage">
                  <div class="field has-addons">
                    <div class="control">
                      <input class="input" type="text" ref="inputNewMessage" v-model="newMessage" autofocus placeholder="Enter username">
                    </div>
                    <div class="control">
                      <a type="submit" class="btn-grad-lightgreen m-0 inline-input-btn">
                        Send
                      </a>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="main-content">
          <div class="card-header has-background-phoenix-start">
            <p class="card-header-title has-text-white">
              Contacts
            </p>
          </div>
          <div class="card main-card flex-body">
            <div class="card-content main-card flex-body main-content has-height-100 p-2">
              <div class="columns is-mobile">
                <div class="column is-half">
                  <div class="box p-2 message-friend">
                    I'm in a box.
                  </div>
                  <div class="box p-2" style="visibility: hidden">
                    I'm in a box.
                  </div>
                  <div class="box p-2 message-friend">
                    I'm in a box.
                  </div>
                  <div class="box p-2 message-friend">
                    I'm in a box.
                  </div>
                  <div class="box p-2 message-friend">
                    I'm in a box.
                  </div>
                </div>
                <div class="column is-half">
                  <div class="box p-2" style="visibility: hidden">
                    I'm in a box.
                  </div>
                  <div class="box p-2 message-my">
                    I'm in a box.
                  </div>
                  <div class="box p-2" style="visibility: hidden">
                    I'm in a box.
                  </div>
                  <div class="box p-2" style="visibility: hidden">
                    I'm in a box.
                  </div>
                  <div class="box p-2" style="visibility: hidden">
                    I'm in a box.
                  </div>
                  <div class="box p-2 message-my">
                    I'm in a box.
                  </div>
                </div>
              </div>
            </div>
            <div class="card-footer">
              <div class="card-footer-item">
                <form @submit.prevent="sendMessage">
                  <div class="field has-addons">
                    <div class="control">
                      <input class="input" type="text" ref="inputNewMessage" v-model="newMessage" autofocus placeholder="Hello!)">
                    </div>
                    <div class="control">
                      <a type="submit" class="btn-grad-lightblue m-0 inline-input-btn">
                        Send
                      </a>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      str: '',
      five: 0,
      friends: [
        {id: 1, user: 'first_user', online: true},
        {id: 2, user: 'second_user', online: true},
        {id: 3, user: 'third_user', online: false},
        {id: 4, user: 'fourth_user', online: false},
        {id: 5, user: 'fifth_user', online: false},
        {id: 6, user: 'first_user', online: true},
        {id: 7, user: 'second_user', online: true},
        {id: 8, user: 'third_user', online: false},
        {id: 9, user: 'fourth_user', online: false},
        {id: 10, user: 'fifth_user', online: false},
        {id: 11, user: 'first_user', online: true},
        {id: 12, user: 'second_user', online: true},
        {id: 13, user: 'third_user', online: false},
        {id: 14, user: 'fourth_user', online: false},
        {id: 15, user: 'fifth_user', online: false},
        {id: 16, user: 'first_user', online: true},
        {id: 17, user: 'second_user', online: true},
        {id: 18, user: 'third_user', online: false},
        {id: 19, user: 'fourth_user', online: false},
        {id: 20, user: 'fifth_user', online: false},
      ],
      newMessage: '',
    }
  },
  beforeMount() {
    if (!this.$store.state.isAuthenticated) {
      this.$router.push('/log-in')
    }
    document.title = 'ChatVerse'
  },
  methods: {
    sendMessage() {
      this.$refs.inputNewMessage.focus()
      this.newMessage = ''
    }
  }
}
</script>

<style scoped>

</style>