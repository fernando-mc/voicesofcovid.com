<template>
    <div>
        <div class="submit-box" id="form-div">
            <div class="ui brown top attached segment">
                <h3>  Share your story:</h3>
            </div>
            <form class="ui equal width attached segment form" id="submission">
                <div class="four fields">
                    <div class="field">
                    <label for="first_name">First name:</label>
                    <input type="text" class="form-control" id="first_name" placeholder="Jasmine" name="first_name">
                    </div>
                    <div class="field">
                    <label for="job">Job:</label>
                    <input type="text" class="form-control" id="job" placeholder="Nurse" name="job">
                    </div>
                    <div class="field">
                    <label for="description">Description:</label>
                    <input type="text" class="form-control" id="description" placeholder="What's your story?" name="description">
                    </div>
                </div>
                <div class="ui two column centered grid">
                    <file-select v-model="file"></file-select>
                </div>
                <br>
                <div class="ui two column centered grid">
                    <div class="one column row">
                    <div class="right floated item">
                        <vue-recaptcha sitekey="6LfBV-YUAAAAAC2F4BdtYjZB72gCuP-aFRd0F_N7"></vue-recaptcha>
                    </div>
                    </div>
                    <div class="one column row">
                    <button type="submit" class="ui huge blue button">Submit</button>
                    <div class="ui error message">
                        <div id='error-message' style="color: red"></div>
                    </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import VueRecaptcha from 'vue-recaptcha';
import FileSelect from './FileSelector.vue'

export default {
  name: 'SubmitBox',
  components: {
      VueRecaptcha,
      FileSelect,
  },
  data () {
    return {
        recordAudio: false,
        file: null,
    }
  },
}
</script>

<style scoped>
.ar-recorder__records-limit {
    margin-top: 28px;
}
</style>