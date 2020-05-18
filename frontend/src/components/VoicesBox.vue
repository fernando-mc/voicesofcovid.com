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
        <InstantSearch/>
      </div>
    </div>
</template>

<script>
import InstantSearch from './InstantSearch.vue'

export default {
  name: 'VoicesBox',
  components: {
    InstantSearch,
  }
}
</script>
