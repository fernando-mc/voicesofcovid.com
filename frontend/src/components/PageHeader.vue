<template>
  <div class="ui top fixed horizontal menu">
    <div class="item">
      <h2>Voices of COVID-19</h2>
    </div>
    <div class="item">
      <a v-on:click="showLearnMore()">Learn More</a>
    </div>
    <div class="item">
      <a v-on:click="showSubmissionGuidelines()">Submission Guidelines</a>
    </div>
    <div class="item">
      <a v-on:click="showRecordingModal()">Recording Tool</a>
    </div>

    <div v-show="learnMoreModalVisibility" class="ui active modal">
      <i v-on:click="hideLearnMore()" class="close icon"></i>
      <div class="header">
        About Voices of COVID-19
      </div>
      <div class="content">
        <div class="description">
          <p>Voices of COVID-19 was inspired by listening to the stories and experience of people impacted by COVID-19.</p>
          <p>Given our inability to really be physically around each other in this time, I wanted to give us an outlet to share and hear stories about our experiences.</p>
          <p>If you'd like an example, you can listen to other stories here or<a href="https://theintercept.com/2020/04/01/essential-workers-and-the-reverse-robin-hood-coronavirus-bailout/" target="_blank"> this episode of The Intercepted Podcast</a> starting at 44:41.</p>
          <br>
        </div>
      </div>
    </div>

    <div v-show="submissionGuidelinesModalVisibility" class="ui active modal">
      <i v-on:click="hideSubmissionGuidelines()" class="close icon"></i>
      <div class="header">
        Submission Guidelines
      </div>
      <div class="content">
        <div class="description">
          <p>First off, if you're considering submitting your story - thank you!</p>
          <p>If you decide to submit, we require that you acknolwedge that you are releasing your submission to the <a href="https://fairuse.stanford.edu/overview/public-domain/welcome/" target="_blank"> public domain</a>. Essentially, this means that you give up all rights to the recording and anyone can use it any way they want.</p>
          <p>This allows anyone and everyone to share your story or repurpose it. It also allows us to edit the story - which we will do carefully and dilligently if we feel we need to before releasing it to curate the collected voices more effectively.</p>
          <p>If you have any questions, don't hesitate to <a href="https://twitter.com/fmc_sea">reach out to me</a>.</p>
          <br>
        </div>
      </div>
    </div>

    <div v-show="recordingModalVisibility" class="ui active modal">
      <i v-on:click="hideRecordingModal()" class="close icon"></i>
      <div class="header">
        Record your audio and select the recording to listen to or download it.
      </div>
      <div class="content">
        <div class="ui grid">
          <audio-recorder
            :attempts="1"
            :time="2"
            :show-upload-button="false"
            :after-recording="downloadRecording"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageHeader',
  methods: {
    downloadRecording() {
      console.log(this)
    },
    showLearnMore() { 
      if (this.learnMoreModalVisibility == false){ 
        this.learnMoreModalVisibility = true;
      }
    },
    hideLearnMore(){
      if (this.learnMoreModalVisibility == true) {
        this.learnMoreModalVisibility = false;
      }
    },
    showSubmissionGuidelines() { 
      if (this.submissionGuidelinesModalVisibility == false){ 
        this.submissionGuidelinesModalVisibility = true;
      }
    },
    hideSubmissionGuidelines(){
      if (this.submissionGuidelinesModalVisibility == true) {
        this.submissionGuidelinesModalVisibility = false;
      }
    },
    showRecordingModal() { 
      if (this.recordingModalVisibility == false){ 
        this.recordingModalVisibility = true;
      }
    },
    hideRecordingModal() {
      if (this.recordingModalVisibility == true) {
        this.recordingModalVisibility = false;
      }
    },
  },
  data () {
    return {
      learnMoreModalVisibility: false,
      submissionGuidelinesModalVisibility: false,
      recordingModalVisibility: false,
    }
  }
}
</script>

<style scoped>
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
