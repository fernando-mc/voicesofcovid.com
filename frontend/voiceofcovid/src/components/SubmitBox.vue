<template>
    <div>
        <div class="ui grid">
            <div class="row mobile only">
                <br>
                <br>
            </div>
        </div>
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
                <div class="field">
                <label for="language">Language:</label>
                <select class="ui selection dropdown" id="gender">
                    <option value="">Select language</option>
                    <option value="english">English</option>
                    <option value="espanol">Español</option>
                    <option value="Other">Other</option>
                </select>
                </div>
            </div>
            <div class="ui two column centered grid">
                <div class="one column row">
                <div class="ui action input">
                    <input id="voicefileupload" type="text" placeholder="Upload your story" readonly>
                    <input id="voicefile" type="file">
                    <div id="voicefileupload" class="ui icon button">
                    <i id="voicefileuploadicon" class="upload icon"></i>
                    </div>
                </div>
                </div>
            </div>
            <br>
            <div class="ui two column centered grid">
                <div class="one column row">
                <div class="right floated item">
                    <div class="g-recaptcha" data-sitekey="6LfBV-YUAAAAAC2F4BdtYjZB72gCuP-aFRd0F_N7"></div>
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
export default {
  name: 'SubmitBox'
}
</script>
