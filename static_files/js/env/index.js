doAjaxCall = function() {
			id = $(this).attr('id')
			url = "http://127.0.0.1:8080" + id
			$(document).ajaxStart(function(){
				$('#pleaseWaitDialog').modal('show');
			});
		
			$.ajax({
				url: url,
				dataType: 'html',
				success: function(data){
					$('#content').html(data);
					$('#pleaseWaitDialog').modal('hide');
					$("input").bind("click",doAjaxCall);
				},
				error: function(error) {
					data = "<div class='alert alert-warning' role='alert'>"+error+" ..</div>"
					$('#home_content').html(data);
					$('#pleaseWaitDialog').modal('hide');
				},
			});
	return false;
};

$(document).ready(function(){
	$("input").bind("click",doAjaxCall);
});