<template>
  <div class="ui grid">
    
      <label class="file-select">
        <div class="select-button">
          <span v-if="value">Selected File: {{value.name}}</span>
          <span v-else>Upload File <i class="upload icon"></i></span>
        </div>
        <input type="file" @change="handleFileChange"/>
      </label>

  </div>
</template>

<script>
export default {
  props: {
    value: File
  },
  methods: {
    handleFileChange(e) {
      this.$emit('input', e.target.files[0])
    },
  }
}
</script>

<style scoped>
.file-select {
    margin-top: 1em;
}

.file-select > .select-button {
  padding: 1rem;

  color: white;
  background-color: #2EA169;

  border-radius: .3rem;

  text-align: center;
  font-weight: bold;
}

.file-select > input[type="file"] {
  display: none;
}

.ui.top.fixed {
  background: #E9DCBA;
  margin-bottom: 100px;
}

.ui.modal {
  top: 10%;
}

.close.icon {
  color: black;
  top: 0;
  right: 0;
}
</style>