$(document).ready(function() {
    loaddata(renderData);
});

function createProgressbar(id, duration, callback) {
  var progressbar = document.getElementById(id);
  progressbar.className = 'progressbar';
  var progressbarinner = document.createElement('div');
  progressbarinner.className = 'inner';
  progressbarinner.style.animationDuration = duration;

  if (typeof(callback) === 'function') {
    progressbarinner.addEventListener('animationend', callback);
  }

  progressbar.appendChild(progressbarinner);

  progressbarinner.style.animationPlayState = 'running';
}


var html = `<div class="col-sm-4 col-md-4" id="card-0">
    <div class="card mb-4 shadow-sm">
        <img id="img-card-0" class="img-thumbnail"  src="" name="card-0"/>
        <audio id="audio-card-0" src=""></audio>
        <div class="mycard" id="text-card-0">
        </div>
    </div>
</div>

<div class="col-sm-4 col-md-4" id="card-1">
    <div class="card mb-4 shadow-sm">
        <img id="img-card-1" class="img-thumbnail"  src="" name="card-1"/>
        <audio id="audio-card-1" src=""></audio>
        <div class="mycard" id="text-card-1">
        </div>
    </div>
</div>

<div class="col-sm-4 col-md-4" id="card-2">
    <div class="card mb-4 shadow-sm">
        <img id="img-card-2" class="img-thumbnail"  src="" name="card-2"/>
        <audio id="audio-card-2" src=""></audio>
        <div class="mycard" id="text-card-2">
        </div>
    </div>
</div>

<div class="col-sm-4 col-md-4" id="card-3">
    <div class="card mb-4 shadow-sm">
        <img id="img-card-3" class="img-thumbnail"  src="" name="card-3"/>
        <audio id="audio-card-3" src=""></audio>
        <div class="mycard" id="text-card-3">
        </div>
    </div>
</div>

<div class="col-sm-4 col-md-4" id="card-4">
    <div class="card mb-4 shadow-sm">
        <img id="img-card-4" class="img-thumbnail"  src="" name="card-4"/>
        <audio id="audio-card-4" src=""></audio>
        <div class="mycard" id="text-card-4">

        </div>
    </div>
</div>

<div class="col-sm-4 col-md-4" id="card-5">
    <div class="card mb-4 shadow-sm">
        <img id="img-card-5" class="img-thumbnail"  src="" name="card-5"/>
        <audio id="audio-card-5" src=""></audio>
        <div class="mycard" id="text-card-5">
        </div>
    </div>
</div>
<input type="hidden" id="value-card-0" value="">
<input type="hidden" id="value-card-1" value="">
<input type="hidden" id="value-card-2" value="">
<input type="hidden" id="value-card-3" value="">
<input type="hidden" id="value-card-4" value="">
<input type="hidden" id="value-card-5" value="">`


function loaddata(renderData) {
  if (usertoken !='Token ') {
        var settings = {
      "url": "https://www.hieubn.com/api/v1/englishapp/",
      "method": "GET",
      "timeout": 0,
      "headers": {
        "Authorization": usertoken
      },
    };
  } else {
      var settings = {
      "url": "https://www.hieubn.com/api/v1/englishapp/",
      "method": "GET",
      "timeout": 0,
    };
  }

  $.ajax(settings).done(function (context) {
    renderData(context)
  }).fail(function() {
      setTimeout(function() {loaddata(renderData)}, 500)
  });
}

function renderData(context) {

  $("#gameboard").html(html)
  $(".inner").remove()

  createProgressbar('progressbar', '10s', function() {
    loaddata(renderData);
    $(".inner").remove()
  });

  window.private_key = context['private_key']
  $("#myanswer").text(context['nana'])
  $("#score").text(context['score'])
  for (i=0;i<=5;i++) {
    $("#img-card-"+i).attr("src", context['cards'][i]['card_pic'])
    $("#audio-card-"+i).attr("src", context['cards'][i]['card_voice'])
    $("#span-card-"+i).text(context['cards'][i]['card_name'])
    $("#value-card-"+i).attr("value", context['cards'][i]['card_name'])
  }
      $("img").click(function() {
        const key = $('#myanswer').text()
        var value = document.getElementById('value-'+this.name).value
        var text = document.getElementById('span-'+this.name)
        var audio = document.getElementById('audio-'+this.name);
        audio.play();

        if (value == key) {
          if (!(typeof(text) != 'undefined' && text != null)) {
              document.getElementById(this.name).className = "mx-auto col-md-4";
              $("div.col-sm-4.col-md-4").remove()

              if (usertoken != 'Token ') {
                  $("#scoreupdate").css("color", "green");
                  $("#scoreupdate").text("+30");
                  setTimeout(function(){$("#scoreupdate").text("")}, 500)
                  const scored = $("#score").text();
                  var scoredd = parseInt(scored) + 30
                  setTimeout(function() {$("#score").text(scoredd)}, 500)

                  var form = new FormData();
                  form.append("answer", "dung");
                  form.append("detected_key", window.private_key);

                  var settings = {
                    "url": "https://www.hieubn.com/api/v1/englishscore/",
                    "method": "POST",
                    "timeout": 0,
                    "headers": {
                      "Authorization": usertoken,
                    },
                      "processData": false,
                      "mimeType": "multipart/form-data",
                      "contentType": false,
                      "data": form
                    };

                  $.ajax(settings).done(function (response) {
                  });
                };
              }

            $(".inner").remove()
            audio.onended = setTimeout(function(){loaddata(renderData)}, 500);
        } else {
          if (!(typeof(text) != 'undefined' && text != null)) {
            if (usertoken != 'Token '){
              $("#scoreupdate").css("color", "red")
              $("#scoreupdate").text("-20");
              setTimeout(function(){$("#scoreupdate").text("")}, 500)
              const scores = $("#score").text();
              var scoress = parseInt(scores) - 20
              setTimeout(function() {$("#score").text(scoress)}, 500)
              var form = new FormData();
              form.append("answer", "sai");
              form.append("detected_key", window.private_key);

              var settings = {
                "url": "https://www.hieubn.com/api/v1/englishscore/",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Authorization": usertoken,
                },
                "processData": false,
                "mimeType": "multipart/form-data",
                "contentType": false,
                "data": form
              };

              $.ajax(settings).done(function (response) {

              });
            }
          }
        }
        var span = `<span id="span-`+this.name+`" class="card-text" style="color: green">`+`<center>`+value+`</center>`+`</span>`
        $('#text-'+this.name).html(span)
        
    });
}