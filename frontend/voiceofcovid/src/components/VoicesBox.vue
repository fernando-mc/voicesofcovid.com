<template>
    <div class="rates-box">
      <div class="ui purple top attached segment">
        <div class="ui stackable grid">
          <div class="five wide column">
            <h3>Listen to other stories:</h3>
          </div>
        </div>
      </div>
      <div class="ui attached segment">
        <br>
        <div class="ui three column grid">
          <div class="ui cards" id="voices">
              <VoicesCard 
                v-for="card in cardsData"
                v-bind:key="card.id"
                v-bind:card="card"
                >
              </VoicesCard>
          </div>
          <br>
        </div>
      </div>
    </div>
</template>

<script>
import VoicesCard from './VoicesCard.vue'

export default {
  name: 'VoicesBox',
  components: {
    VoicesCard,
  },
  data: function () {
    return {
      cardsData: [
        {
          id: 'm1-01-trailer.mp3',
          name : 'Fernando',
          job : 'Nurse',
          description : 'super good at nursing',
          language : 'en',
          url: 'https://s3-us-west-2.amazonaws.com/voicesofcovid.com/m1-01-trailer.mp3'
        },{
          id: 'm1-01-trailer.mp3',
          name : 'Fernando',
          job : 'Nurse',
          description : 'super good at nursing',
          language : 'en',
          url: 'https://s3-us-west-2.amazonaws.com/voicesofcovid.com/m1-01-trailer.mp3'
        }
      ]
    }
  }
}
</script>
