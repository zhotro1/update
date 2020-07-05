$(document).ready(function() {
    $("img").click(function() {
        console.log(this.name)
        const key = $('#mycontent').text()
        console.log(key)
        if (this.name == key) {
            setTimeout(function(){location.reload()}, 1500);
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