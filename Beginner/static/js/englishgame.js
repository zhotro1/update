$(document).ready(function() {
    var token_user = 'Token '+token
    $("img").click(function() {
        const key = $('#mycontent').text()
        if (this.name == key) {
          var form = new FormData();
          form.append("answer", "dung");
          form.append("detected_key", private_key);

          var settings = {
            "url": "http://www.hieubn.com/api/v1/englishscore/",
            "method": "POST",
            "timeout": 1000,
            "headers": {
              "Authorization": token_user,
            },
            "processData": false,
            "mimeType": "multipart/form-data",
            "contentType": false,
            "data": form
          };

          $.ajax(settings).done(function (response) {
            console.log(response)
          });
            setTimeout(function(){location.reload()}, 1500);
        } else {
          if (document.getElementById("span"+this.name).classList.contains("text-hide")) {
            var form = new FormData();
            form.append("answer", "sai");
            form.append("detected_key", private_key);

            var settings = {
              "url": "http://www.hieubn.com/api/v1/englishscore/",
              "method": "POST",
              "timeout": 1000,
              "headers": {
                "Authorization": token_user,
              },
              "processData": false,
              "mimeType": "multipart/form-data",
              "contentType": false,
              "data": form
            };

            $.ajax(settings).done(function (response) {
              console.log(response)
            });
          }
        }
        document.getElementById("span"+this.name).className = "card-text text-show"
        var audio = document.getElementById(this.name)
        audio.play()
    })

});

function createProgressbar(id, duration, callback) {
  // We select the div that we want to turn into a progressbar
  var progressbar = document.getElementById(id);
  progressbar.className = 'progressbar';

  // We create the div that changes width to show progress
  var progressbarinner = document.createElement('div');
  progressbarinner.className = 'inner';

  // Now we set the animation parameters
  progressbarinner.style.animationDuration = duration;

  // Eventually couple a callback
  if (typeof(callback) === 'function') {
    progressbarinner.addEventListener('animationend', callback);
  }

  // Append the progressbar to the main progressbardiv
  progressbar.appendChild(progressbarinner);

  // When everything is set up we start the animation
  progressbarinner.style.animationPlayState = 'running';
}

addEventListener('load', function() {
    createProgressbar('progressbar', '20s', function() {
    location.reload();
  });
});