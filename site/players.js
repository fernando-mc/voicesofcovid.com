testVoices = [
  {
    id: 'm1-01-trailer.mp3',
    name : 'Fernando',
    job : 'Nurse',
    description : 'super good at nursing',
    language : 'en',
    url: 'https://s3-us-west-2.amazonaws.com/voicesofcovid.com/m1-01-trailer.mp3'
  },
  {
    id: '178tyugadsih',
    name : 'Fernando',
    job : 'Nurse',
    description : 'super good at nursing',
    language : 'en',
    url: 'https://cdn.plyr.io/static/demo/Kishi_Bashi_-_It_All_Began_With_a_Burst.mp3'
  }
]

function writeVoices(voices){
  let finalCards = ''
  for (i = 0; i < voices.length; i++){
    finalCards += `
      <div class="card">
        <div class="content">
          <div class="header">
            ` + voices[i].name + ` 
          </div>
          <div class="meta">
            ` + voices[i].job + ` | ` + voices[i].language + `
          </div>
          <div class="description">
            ` + voices[i].description + `
          </div>
        </div>
        <audio crossorigin playsinline class="audioplayer" controls>
            <source src="` + voices[i].url + `" type="audio/mp3">
          </audio>
        <div class="extra content">
          
        </div>
    </div>
      `;
    }
  document.getElementById("voices").innerHTML += finalCards
  const players = Array.from(document.getElementsByClassName("audioplayer")).map(p => new Plyr(p));
}


writeVoices(testVoices)