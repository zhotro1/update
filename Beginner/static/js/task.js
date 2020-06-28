$("body").css("background-image", "url('/static/img/wa.png')");
var myVar = $("#myVar").val();

$("div#mynavbar").after(myVar);

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

$(function () {
    $('#mytable').on('show.bs.collapse', function () {
    $('#mytable .in').collapse('hide');
    });

});

$("#annav").click(function(){
    $("nav").remove();
});

function checkForm(){
    var id = '_' + Math.random().toString(36).substr(2, 9);
    var idd = '_' + Math.random().toString(36).substr(2, 9);
    var iddd = '_' + Math.random().toString(36).substr(2, 9);
    var title =document.getElementById('id_title').value;
    var descriptions =document.getElementById('id_description').value;
    var priority =document.getElementById('id_priority').value;
    var html = `<div id=`+iddd.toString()+` class="card btn-block" style="margin-top: 10px; border-radius: 5px; padding: 10px; background-color: #fafafa">
        <div class="row">
            <div class="col-9">

                <a href="" id=`+idd.toString()+` data-toggle="collapse" data-target="#`+id.toString()+`" style="text-decoration: none;" class="`+ priority.toString()+` collapsed aa" aria-expanded="false">` + title.toString() + `</a>

                <div class="collapse" id="`+id.toString()+`" style="">
                      <div class="" style="border-radius: 0;">
                        <div class="row">
                            <div class="col" id="descriptions">`+
                                descriptions.toString()
                            +`</div>
                        </div>
                      </div>
                    </div>

                </div>
                <div class="col-3">
                    <div class="btn-group float-right" role="group">
                        <a href="javascript:hoanthanh('`+idd.toString()+`')" class="float-right" data-toggle="tooltip" title="Hoàn thành?">&#10004;</a>
                        <a href="javascript:xoa('`+iddd.toString()+`')" class="float-right" style="padding-left: 10px;" data-toggle="tooltip" title="Xóa">&#10007;</a>
                    </div>
                </div>
            </div>
        </div>`;

    if (priority.toString() == 'adanger') {
        document.querySelector('#mytablea').insertAdjacentHTML(
            'afterbegin', html
            );
    };

    if (priority.toString() == 'bwarning') {
        document.querySelector('#mytableb').insertAdjacentHTML(
            'afterbegin', html
            );
    };

    if (priority.toString() == 'csuccess') {
        document.querySelector('#mytablec').insertAdjacentHTML(
            'afterbegin', html
            );
    };
    
};

function hoanthanh(id) {
  var st = document.getElementById(id).style.textDecoration;
  if (st === "line-through") {
    document.getElementById(id).style.textDecoration = ""
  } else{ document.getElementById(id).style.textDecoration = "line-through"}
};

function xoa(id) {
  document.getElementById(id).remove()
};