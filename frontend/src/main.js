import Vue from 'vue'
import App from './App.vue'
import InstantSearch from 'vue-instantsearch';
import VuePlyr from 'vue-plyr'
import AudioRecorder from 'vue-audio-recorder'
 
Vue.use(AudioRecorder)

Vue.config.productionTip = false
Vue.use(InstantSearch);
Vue.use(VuePlyr, {
  plyr: {
    fullscreen: { enabled: false }
  },
  emit: ['ended']
})

new Vue({
  render: h => h(App),
}).$mount('#app')
