$(document).ready(function() {
	base();
	initdocument();
});


function initdocument() {
    $("iframe").height($(window).height());
    $("iframe").width($("body").width());
    $(window).resize(initdocument());

};

function base() {
    $("body").css("overflow", "hidden")
    $("iframe").css("overflow", "auto")
	$("body").css('background','#FBF0D9').css('color','#5F4B32')
	
}