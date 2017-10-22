$(function() {	
    $("input").on("click", function() {
		id = $(this).attr('id')
		url = "http://127.0.0.1:8080" + id
			
		$.ajax({
            url: url,
			dataType: 'html',
			success: function(data){
				$('body').html(data)
			},
		});
    });
});