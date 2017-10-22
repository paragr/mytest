changeActiveClass = function() {
			$('.app_home').removeClass('active');
			$(this).addClass('active');
			url =  "http://127.0.0.1:8080/" + $(this).attr('id') + "/";
			$.ajax({
				url: url,
				dataType: 'html',
				success: function(data){
					$('#home_content').html(data);
				},
				error: function(error) {
					data = "<div class='alert alert-warning' role='alert'>"+error+"\n\nDevelopment in Progress ..</div>"
					$('#home_content').html(data);
				},
			});
	return false;
};

$(document).ready(function(){
	$(".app_home").bind("click",changeActiveClass);
	return false;
});