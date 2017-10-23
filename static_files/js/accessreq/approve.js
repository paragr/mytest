function getCookie(name) {
// get the csrf token

    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

approveRequest = function() {
			var url = $(this).attr('id');
			var dataString = 'csrfmiddlewaretoken=' + getCookie('csrftoken');
								
			$.ajax({
				url: url,
				type: "GET",
				data: dataString,
				success: function(data){
					$("li[id*='accessreq/view_requests_list']").trigger('click');
				},
				error: function(error) {
					alert('error occured during ajax call');
				},
			});
	return false;
};

$(document).ready(function(){
	$("input[id*='accessreq/approved']").bind("click",approveRequest);
});