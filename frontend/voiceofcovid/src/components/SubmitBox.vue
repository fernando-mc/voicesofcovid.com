<template>
    <div class="submit-box">
        <div v-show="!show_submit_box" class="ui brown top attached segment">
            <h3>Thanks for sharing your story!</h3>
        </div>
        <div v-show="show_submit_box" class="ui brown top attached segment">
            <h3>  Share your story:</h3>
        </div>
        <form v-show="show_submit_box" class="ui equal width attached segment form" id="submission">
            <div class="four fields">
                <div class="field">
                <label for="first_name">First name:</label>
                <input v-model="first_name" type="text" class="form-control" placeholder="Jasmine">
                </div>
                <div class="field">
                <label for="job">Job:</label>
                <input v-model="job" type="text" class="form-control" placeholder="Nurse">
                </div>
                <div class="field">
                <label for="description">Description:</label>
                <input v-model="description" type="text" class="form-control" placeholder="What's your story?">
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
                <button v-on:click.prevent="submitForm()" type="submit" class="ui huge blue button">Submit</button>
                <div class="ui error message">
                    <div id='error-message' style="color: red"></div>
                </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import VueRecaptcha from 'vue-recaptcha';
import FileSelect from './FileSelector.vue'
import axios from 'axios'

export default {
  name: 'SubmitBox',
  components: {
      VueRecaptcha,
      FileSelect,
  },
  methods: {
    submitForm () {
        var vm = this;
        var requestPresignedUrlbodyData = {
            "captcha": window.grecaptcha.getResponse(),
            "data": {
                "name": this.first_name, 
                "job": this.job,
                "description": this.description
            }
        }
        var endpointToRequestPresignedUrl = 'https://8h8vhvd4te.execute-api.us-east-1.amazonaws.com/dev/generate'
        var endpointToPostAudioFile = 'https://voicesofcovid.s3.us-east-1.amazonaws.com'
        console.log(window.grecaptcha.getResponse())
        console.log(requestPresignedUrlbodyData)
        axios.post(endpointToRequestPresignedUrl, requestPresignedUrlbodyData)
        .then(function (response) {
            let formData = new FormData();
            for (const field in response.data) {
                formData.append(field, response.data[field]);
            }
            formData.append('file', vm.file);
            axios.post(
                endpointToPostAudioFile,
                formData
            )
            vm.show_submit_box = false
        })
        console.log("yup");
    }
  },
  data () {
    return {
        file: null,
        first_name: null,
        job: null,
        description: null,
        show_submit_box: true,
    }
  },
}
</script>

<style scoped>
.ar-recorder__records-limit {
    margin-top: 28px;
}
</style>