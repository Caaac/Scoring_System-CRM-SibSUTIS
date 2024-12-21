import './assets/main.css'
import 'primevue/resources/themes/aura-light-indigo/theme.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'
import App from '@/App.vue'
import Router from '@/router'

import Axios from '@/api/axios'
import '@/mixins/date'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(Router)
app.use(PrimeVue)
app.use(ToastService)
app.provide('$axios', Axios)

app.mount('#app')

Object.defineProperty(Date.prototype, 'toISOFullDate', {
  enumerable: false,
  value: function () {
    return (
      this.getFullYear() +
      '-' +
      (this.getMonth() + 1).toString().padStart(2, '0') +
      '-' +
      this.getDate().toString().padStart(2, '0')
      + ' '
      + this.getHours().toString().padStart(2, '0')
      + ':'
      + this.getMinutes().toString().padStart(2, '0')
      + ':'
      + this.getSeconds().toString().padStart(2, '0')
    )
  }
})
