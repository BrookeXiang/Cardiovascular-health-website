$(function () {
    var error_age = true;
    var error_statur = false;

    // alert('is action')

    function check_all() {
        $('.msgTips').hide();
        var age = Number($('#age').val());//年龄
        var stature = Number($('#stature').val());//身高
        var weight = Number($('#weight').val());//体重
        var systolicpress = Number($('#systolicpress').val());
        var diastolicpress = Number($('#diastolicpress').val());
        var cholesterol = Number($('#cholesterol').val());
        var bloodglucose = Number($('#bloodglucose').val());

        if (age <= 0 || age > 100) {
            $('#age').next().html('Incorrect age input');
            $('#age').next().show();
            return false;
        }
        if (stature <= 0 || stature > 250) {
            $('#stature').next().html('Incorrect height input');
            $('#stature').next().show();
            return false;
        }
        if (weight <= 0 || weight > 300) {
            $('#weight').next().html('Incorrect weight input');
            $('#weight').next().show();
            return false;
        }
        if (systolicpress <= 0 || systolicpress >= 300) {
            $('#systolicpress').next().html("range 0-300");
            $('#systolicpress').next().show();
            return false;
        }
        if (diastolicpress <= 0 || diastolicpress >= 300) {
            $('#diastolicpress').next().html("range 0-300");
            $('#diastolicpress').next().show();
            return false;
        }
        if (cholesterol <= 0 || cholesterol >= 100) {
            $('#cholesterol').next().html("range 0-100");
            $('#cholesterol').next().show();
            return false;
        }
        if (bloodglucose <= 0 || bloodglucose >= 100) {
            $('#bloodglucose').next().html("range 0-100");
            $('#bloodglucose').next().show();
            return false;
        }
        return true;
    }

    $('#reg_form').submit(function () {
        // alert('action')
        return check_all();
    });
});