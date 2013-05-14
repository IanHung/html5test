
$(document).ready(function () {
	$('.col2').height($('.col1').height()-20);
	$('.col3').height(($('.col1').height()-150));
	$(window).resize(function(){
		$('.col2').height($('.col1').height()-20);
		$('.col3').height(($('.col1').height()-150));
	});
});	
	
