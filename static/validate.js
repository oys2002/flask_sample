function validateUserName(){
var name=document.forms['registrationform']['username'].value;
if (name==''){
    document.getElementById("username").style.border="2px solid red";
    return false
}
}