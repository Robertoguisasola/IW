$(document).ready(function() {
	$("div.cordilleras > a").click(function(e) {
		var contenido = $(this).attr("name");
		contenido = "#" + contenido + "body"
		$(contenido).fadeOut();

	});
});


$(document).ready(function() {
	$("div.cordilleras > a").dblclick(function(e){
		var contenido = $(this).attr("name");
		contenido = "#" + contenido + "body";
		$(contenido).fadeIn();
	});
});