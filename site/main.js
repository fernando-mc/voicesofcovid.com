var API_URL = 'https://r5nj8ccm2c.execute-api.us-west-2.amazonaws.com/dev/voice';
var errorDiv = document.getElementById('error-message')


// function postMetadata() {
//     return {
//         url : 'presignedUrl',
//     };
// }

function getSubmissionData() {
    // Get CAPTCHA 
    const captchtaResponse = grecaptcha.getResponse() || false
    if (!captchtaResponse) {
        errorDiv.innerHTML = 'Complete the Captcha please!'
        return false
    } else {
        var post_data = {
            captcha: captchtaResponse
        };
        const optionalFields = ['name', 'job', 'description', 'language'];
        for (i = 0; i < optionalFields.length; i++) {
            if ($('#' + optionalFields[i]).val()) {
                post_data[optionalFields[i]] = $('#' + optionalFields[i]).val()
            }
        }
        return post_data
    }
}

async function postSubmissionData(data) {
    var response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    var result = await response.json()
    console.log(result)
    return result
}

async function processUpload(data) {
    var voice_file = document.getElementById("voicefile").files[0]
        let formData = new FormData();
          formData.append("voice", voice_file);
          fetch(responseData.url, {method: "POST", body: formData});
        };
        if (responseData.message == 'Captcha Invalid') {
          console.log('The Captcha failed. Please try again!')

    // Let the user know the file is uploaded
    document.getElementById("hr-divider").innerHTML = ""
    document.getElementById("form-div").innerHTML = "<p> Your story is now uploaded! Email voicesofcovid@gmail.com if you have any questions</p>"
}


// Setup Clickable file uploaders
$("#voicefileuploadicon").click(function() {
    $(this).parent().parent().find("input:file").click();
});

$("#voicefileupload").click(function() {
    $(this).parent().find("input:file").click();
});

// Make sure filename gets set in the file input
$('input:file', '.ui.action.input')
    .on('change', function(e) {
        var filename = e.target.files[0].name;
        $('input:text', $(e.target).parent()).val(filename);
});


$('#submission').submit(function (event) {
    event.preventDefault();
    var data = getSubmissionData()
    var presignedUrlData = postSubmissionData(data)
    var result = processUpload(presignedUrlData)
    console.log(result)
})


