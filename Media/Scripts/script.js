$(document).ready(function(){
	/* This function lets you click on a list of images to view details about a particular image */
	$('tr.ad_details').live('click', function(){
		window.location=$(this).attr('my_href');
	});
	
});