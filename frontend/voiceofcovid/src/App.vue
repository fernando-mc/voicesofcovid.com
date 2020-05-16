<template>
  <div id="app">
    <PageHeader/>
    <div class="ui container main-box">
      <SubmitBox/>
      <HorizontalDivider/>
      <VoicesBox/>
    </div>
  </div>
</template>

<script>
import PageHeader from './components/PageHeader.vue'
import SubmitBox from './components/SubmitBox.vue'
import HorizontalDivider from './components/HorizontalDivider.vue'
import VoicesBox from './components/VoicesBox.vue'

export default {
  name: 'App',
  components: {
    PageHeader, 
    SubmitBox,
    HorizontalDivider,
    VoicesBox,
  },
}
</script>

<style>
  .card {
    margin-top: 10px;
  }
  body {
    background-color: #373E58;
  }
  .main-box {
    margin-top: 6rem;
  }
  body>.container {
    padding: 24px;
    background-color: #373E58;
  }
  .hits-box {
    padding: 1px 14px 12px;
  }

body {    
    padding: 1em;
  }
  
  .ui.action.input input[type="file"] {
    display: none;
  }
  
  .ui.top.fixed {
    background: #E9DCBA
  }

  .ui.horizontal.divider {
    color: #E9DCBA;
  }
</style>
