function checkUsername(){
    var username = document.getElementById('username');
    var reg = /^$/;
    var myBool = true;
    if(!reg.test(username.value)){
        myBool = false;
        username.style = 'border: 2px solid red'; 
    }    
}


function checkEmail(){
    var email = document.getElementById('email');
    var reg = /^([0-9]{0,}[a-z]{1,}[0-9]{0,}[._]?)+[@]{1,1}(\w*)(\.\w*){1,3}(\.[A-Z]{1,}){0,4}$/igm;
    myBool = true;
    if(!reg.test(email.value)){
        myBool = false;
        email.style = 'border: 2px solid red;';
    }
}




function triggerClick(){
    document.querySelector('#profileImage').click();
}

function displayImage(e){
    if(e.files[0]){
        var reader = new FileReader();

        reader.onload = function(e){
            document.querySelector('#profileDisplay').setAttribute('srс', e.target.result);
        }
        reader.readAsDataURL(e.files[0]);
    }
}



$(document).ready(function(){
       
    $('.info').load("/infoforguest");
 
 });