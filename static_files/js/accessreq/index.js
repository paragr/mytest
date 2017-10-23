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

raiseRequest = function() {
			var users = $('textarea#id_users_list').val()
			if (users == "") {
				$("textarea#id_users_list").after('<span class="help-inline">Users Required</span>');
				$("textarea#id_users_list").focus();
				return false;
			} else {
				$('.help-inline').remove();
			}
			
			var env = $('input#id_env').val()
			if (env == "") {
				$("input#id_env").after('<span class="help-inline">Group Required</span>');
				$("input#id_env").focus();
				return false;
			} else {
				$('.help-inline').remove();
			}
			
			var dataString = 'users_list='+ users
                                + '&env=' + env
                                + '&csrfmiddlewaretoken=' + getCookie('csrftoken');
			
			$.ajax({
				url: "/accessreq/raise_request/",
				data: dataString,
				type: "POST",
				success: function(data){
					$("li[id*='accessreq/view_requests_list']").trigger('click');
					//$.get('/accessreq/view_requests_list/',function(data){
						//$('#home_content').html(data);
						//$('.app_home').removeClass('active');
						//$("li[id*='accessreq/view_requests_list']").addClass('active');
					//});
				},
				error: function(error) {
					alert('error occured during ajax call');
				},
			});
	return false;
};

$(document).ready(function(){
	$("#raise").bind("click",raiseRequest);
});