$(function(){
	var error_age = true;
	var error_statur = false;

    alret('is action')
	$('#age').blur(function() {
		check_age();
	});

	$('#statur').blur(function() {
		check_statur();
	});


	function check_age(){
		var len = $('#age').val().length;

		if(len==0)
		{
			$('#age').next().html('请输入年龄');
			$('#age').next().show();
            err_age = true;

		}
		else
		{
			err_age = false;
        }
	}
    function check_statur(){
		var len = $('#statur').val().length;

		if(len==0)
		{
			$('#statur').next().html('请输入身高');
			$('#statur').next().show();
            err_age = true;

		}
		else
		{
			err_age = false;
        }
	}

	$('#reg_form').submit(function() {
        alert('action')
		check_age();
		check_statur();


		if(error_age == false && error_statur == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});
});