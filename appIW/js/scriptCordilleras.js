$(document).ready(function() {
	$("div.content > a").click(function(e) {
		var contenido = $(this).attr("name");
		contenido = "#" + contenido + "body"
		$(contenido).fadeOut();
	});
});


$(document).ready(function() {
	$("div.content > a").dblclick(function(e){
		var content = $(this).attr("name");
		contenido = "#" + contenido + "body";
		$(contenido).fadeIn();
	});
});