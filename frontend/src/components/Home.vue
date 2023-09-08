<template>
  <div class="main-absolute">
    <div class="columns is-mobile m-0 has-background-sp has-height-100">
      <div class="column is-two-fifths-mobile is-two-fifths-tablet is-one-fifth-desktop is-one-fifth-fullhd is-one-fifth-widescreen">
        <div class="main-content is-flex is-flex-direction-column">
          <div class="card-header has-background-fresh-oasis">
            <p class="card-header-title has-text-white">
              Contacts
            </p>
          </div>
          <div class="card main-card flex-body has-invisible-scroll has-position-relative">
            <div class="card-content main-card p-2 main-absolute">
              <div v-for="contact in contacts" :key="contact.id">
                <div class="box p-1 my-2" @click="beforeWebsocket(contact.username)">
                  <article class="media">
                    <div class="media-left">
                      <figure class="image is-32x32">
                        <img :src=contact.photo.small_square_crop alt="Image" v-if="contact.photo.small_square_crop">
                        <img src="../assets/no-no-user.jpg" alt="Image" v-else>
                      </figure>
                    </div>
                    <div class="media-content pt-1">
                      <div class="content">
                        <p>
                          <strong>@{{ contact.username }}</strong>
                          <span class="tag is-success is-pulled-right" v-if="contact.is_online">Online</span>
                          <span class="tag is-danger is-pulled-right" v-else>Offline</span>
                        </p>
                      </div>
                    </div>
                  </article>
                </div>
              </div>
            </div>
          </div>
          <div class="card-footer has-background-white">
            <div class="card-footer-item">
              <form @submit.prevent>
                <div class="field has-addons">
                  <div class="control">
                    <input class="input" type="text" v-model="searchUser" placeholder="Enter username">
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


      <div class="column">
        <div class="main-content is-flex is-flex-direction-column">
          <div class="card-header has-background-phoenix-start">
            <p class="card-header-title has-text-white">
              Chat <span class="pl-1" v-if="chatUser2">with <span class="has-text-orange">{{ chatUser2 }}</span></span>
            </p>
          </div>
          <div class="card main-card flex-body has-invisible-scroll has-position-relative">
            <div class="card-content main-card p-2 is-overflow-auto has-invisible-scroll main-absolute" id="chat">
              <div class="" v-for="message in roomMessages" :key="message.id">

                <div class="is-fullwidth space-between" v-if="message.sender===user" style="display: flex">
                  <div class="box chat-message-box p-4 is-invisible w-30"></div>
                  <div class="box chat-message-box p-4 w-70 chat-user-box">
                    {{ message.message }}
                  </div>
                </div>

                <div class="is-fullwidth space-between" v-else style="display: flex">
                  <div class="box chat-message-box p-4 w-70 chat-contact-box">
                    {{ message.message }}
                  </div>
                  <div class="box chat-message-box p-4 is-invisible w-30"></div>
                </div>

              </div>
            </div>
          </div>
          <div class="card-footer has-background-white">
            <div class="card-footer-item">
              <form @submit.prevent="sendMessage">
                <div class="field has-addons">
                  <div class="control">
                    <input class="input" type="text" ref="inputNewMessage" v-model="newMessage" placeholder="Hello!)">
                  </div>
                  <div class="control">
                    <a @click="sendMessage" class="btn-grad-lightblue m-0 inline-input-btn">
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
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      chatSocket: {},
      searchUser: '',
      roomName: '',
      user: '',
      chatUser2: '',
      contacts: [],
      str: '',
      five: 0,
      roomMessages: [],
      newMessage: '',
    }
  },
  beforeMount() {
    if (!this.$store.state.isAuthenticated) {
      this.$router.push('/log-in')
    }
    document.title = 'ChatVerse'
  },
  async mounted() {
    await this.getContacts()
    if (this.contacts) {
      setInterval(() => {
        this.getContactsOnlineStatus()
      }, 120000)
    }
  },
  methods: {
    beforeWebsocket(user2_username) {
      if (this.roomName) {
        this.chatClose()
        this.createNewWebsocket(user2_username)
      } else {
        this.createNewWebsocket(user2_username)
      }
    },
    async createNewWebsocket(user2_username) {
      const user1Username = this.$store.state.username
      this.user = user1Username
      const user2Username = user2_username
      this.chatUser2 = user2Username
      const sortedUsernames = [user1Username, user2Username].sort()
      const roomName = sortedUsernames.join("_")
      this.roomName = roomName
      await this.getRoomMessages(roomName)
      await this.chatScroll()
      this.$refs.inputNewMessage.focus()
      this.chatSocket = new WebSocket(`ws://127.0.0.1:8000/ws/${roomName}/?token=${localStorage.getItem('token')}&user2=${user2Username}`)
      this.chatSocket.onmessage = this.chatOnMessage
      this.chatSocket.onclose = this.chatClose
    },
    async chatOnMessage(e) {
      const data = JSON.parse(e.data)
      if (data.message.length) {
        await this.roomMessages.push({
          'id': data.id,
          'sender': data.username,
          'message': data.message
        })
        await this.chatScroll()
      } else {
        alert('the message was empty')
      }
    },
    chatClose() {
      this.chatSocket = {}
      this.chatUser2 = ''
      this.roomName = ''
      this.roomMessages = []
      console.log('close')
    },
    sendMessage() {
      this.chatSocket.send(JSON.stringify({
        'message': this.newMessage,
        'username': this.$store.state.username,
        'room': this.roomName
      }))
      this.$refs.inputNewMessage.focus()
      this.newMessage = ''
    },
    async getContacts() {
      await axios.get('http://127.0.0.1:8000/api/v1/account/contacts/')
          .then((response) => {
            this.contacts = response.data
          })
          .catch((error) => {
            console.log(error)
          })
    },
    async getRoomMessages(roomName) {
      await axios.get(`http://127.0.0.1:8000/api/v1/room/${roomName}/`)
          .then((response) => {
            const messages = response.data.messages
            if (messages) {
              const sortedMessages = messages.slice().sort((a, b) => a.id - b.id)
              sortedMessages.forEach((message) => {
                this.roomMessages.push(message)
              })
            } else {
              return []
            }
          })
          .catch((error) => {
            console.log(error)
          })
    },
    async getContactsOnlineStatus() {
      await axios.get('http://127.0.0.1:8000/api/v1/account/contacts/online-status/')
          .then((response) => {
            const statuses = response.data
            this.contacts.forEach((contact) => {
              statuses.forEach((status) => {
                if (contact.id === status.id) {
                  contact.is_online = status.is_online
                }
              })
            })
          })
          .catch((error) => {
            console.log(error)
          })
    },
    chatScroll() {
      const elem = document.getElementById('chat')
      elem.scrollTop = elem.scrollHeight
    }
  }
}
</script>

<style scoped>

</style>