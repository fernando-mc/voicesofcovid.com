function postMetadata() {
    return {
        url : 'presignedUrl',
    };
}


$("#voicefileuploadicon").click(function() {
    $(this).parent().parent().find("input:file").click();
  });
  $("#voicefileupload").click(function() {
    $(this).parent().find("input:file").click();
  });

  $('input:file', '.ui.action.input')
    .on('change', function(e) {
      var name = e.target.files[0].name;
      $('input:text', $(e.target).parent()).val(name);
    });
  
  const optionalFields = ['name', 'job', 'description', 'language'];
  var API_URL = 'https://REPLACE_ME.execute-api.us-east-1.amazonaws.com/dev/validate';

  var errorDiv = document.getElementById('error-message')

  $('#submission').submit(function (event) {
    event.preventDefault();

    const captchtaResponse = grecaptcha.getResponse() || false

    if (!captchtaResponse) {
      errorDiv.innerHTML = 'Complete the Captcha please!'
      return false
    }

    var post_data = {
      captcha: captchtaResponse
    };
      
    for (i = 0; i < optionalFields.length; i++) {
      if ($('#' + optionalFields[i]).val()) {
        post_data[optionalFields[i]] = $('#' + optionalFields[i]).val()
      }
    }


    const data = { username: 'example' };
    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
        var voice_file = document.getElementById("voicefile").files[0]
        document.getElementById("hr-divider").innerHTML = ""
        document.getElementById("form-div").innerHTML = "<p> Your story is being uploaded now</p>"
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
          
          
          
          let formData = new FormData();
          formData.append("voice", voice_file);
          fetch(responseData.url, {method: "POST", body: formData});
        };
        if (responseData.message == 'Captcha Invalid') {
          console.log('The Captcha failed. Please try again!')
        };
      },
    })
  })
