
$(document).ready(function () {
	$('.col2').height($('.col1').height()-20);
	$('.col3').height(($('.col1').height()-150));
	$(".gardenPlant").width($(".category").width());
	$(window).resize(function(){
		$('.col2').height($('.col1').height()-20);
		$('.col3').height(($('.col1').height()-150));
		$(".gardenPlant").width($(".category").width());
		$(".gardenPlot").masonry("reload");
	});
	
});	
	
