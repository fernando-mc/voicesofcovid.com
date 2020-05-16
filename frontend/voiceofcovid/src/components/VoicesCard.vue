<template>
    <div class="card">
        <div class="content">
          <div class="header">
            {{ card.name }}
          </div>
          <div class="meta">
            {{ card.job }} | {{ card.language }}
          </div>
          <div class="description">
            {{ card.description }}
          </div>
        </div>
        <audio crossorigin playsinline class="audioplayer" controls>
            <source :src="card.url" type="audio/mp3">
          </audio>
        <div class="extra content">

        </div>
    </div>
</template>

<script>
export default {
  name: 'VoicesCard',
  props: ['card']
}
</script>
