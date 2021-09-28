
$('label[for="id_approved"]').css("visibility", "hidden")
$("#id_approved").css("visibility", "hidden");

if (getCookie('permissions').includes('allowApprove'))
{
    $("#id_approved").css("visibility", "visible");
    $("#id_approved").prop( "checked", true );
}
