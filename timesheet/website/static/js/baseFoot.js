adminVisibility = $("#adminVisibility").val()
allowApprove = $("#allowApprove").val()
$('#AdminLink').css("visibility", adminVisibility) 

function getCookie(name)
  {
    var regularExpression = new RegExp(name + "=([^;]+)");
    var value = regularExpression.exec(document.cookie);
    return (value != null) ? unescape(value[1]) : null;
  }
  