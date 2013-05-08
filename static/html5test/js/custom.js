$(document).ready(function () {
	$('.col2').height($('.col1').height()-20);
	$(window).resize(function(){
		$('.col2').height($('.col1').height()-20);
	});
});