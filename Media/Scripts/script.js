$(document).ready(function(){
	$('tr.ad_details').live('click', function(){
		window.location=$(this).attr('my_href');
	});
	
	
});