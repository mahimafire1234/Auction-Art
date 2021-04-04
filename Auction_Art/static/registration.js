var uname_input=document.getElementById("username");
var fname_input=document.getElementById("firstname");
var lname_input=document.getElementById("lastname");
var email_input=document.getElementById("email");
var pass_input=document.getElementById("password");
var repass_input=document.getElementById("repassword");;
var submit=document.getElementById("submit");
var errormess=document.getElementsByClassName("error");

submit.addEventListener("click",showerror);
uname_input.addEventListener("keyup",function firsterr(){
    if(uname_input.value==="" ){

        errormess[0].innerHTML="User name is empty";
        uname_input.style.borderColor="red";
    }else{
        uname_input.style.borderColor="green";
        errormess[0].innerHTML="";

    }
});
fname_input.addEventListener("keyup",function firsterr(){
    if(fname_input.value==="" ){

        errormess[1].innerHTML="First name is empty";
        fname_input.style.borderColor="red";
    }else{
        fname_input.style.borderColor="green";
        errormess[1].innerHTML="";

    }
});

lname_input.addEventListener("keyup",function lasterr(){
    if(lname_input.value==="" ){

        errormess[2].innerHTML="Last name is empty";
        lname_input.style.borderColor="red";

    }else{
        lname_input.style.borderColor="green";
        errormess[2].innerHTML="";

    }
});

email.addEventListener("keyup",function emailerr(){
    if(email_input.value==="" ){


        errormess[3].innerHTML="Email field is  empty";
        email_input.style.borderColor="red";


    }else{
        email_input.style.borderColor="green";
        errormess[3].innerHTML="";

    }
});
pass_input.addEventListener("keyup",function passerr(){
    if(pass_input.value==="" ){
        errormess[4].innerHTML="Password field is  empty";
        pass_input.style.borderColor="red";


    }else if(pass_input.value.length<8){
        errormess[4].innerHTML="Password  should be 8 to 19 characters long ";
        pass_input.style.borderColor="red";

    }else if(pass_input.value.length>20){
        errormess[4].innerHTML="Password is too long";
        pass_input.style.borderColor="red";

    }
    else{
        pass_input.style.borderColor="green";
        errormess[4].innerHTML="";

    }
});
repass_input.addEventListener("keyup",function repasserr(){
    if(repass_input.value==="" ){
        errormess[5].innerHTML="Password confirmation field is empty";
        repass_input.style.borderColor="red";


    }else if(repass_input.value!=pass_input.value){
        errormess[5].innerHTML="Matching Passwords. They dont match ";
        repass_input.style.borderColor="red";
    }
    else{
        repass_input.style.borderColor="green";
        errormess[5].innerHTML="";

    }
});


function showerror($event){
    let items=[uname_input,fname_input,lname_input,email_input,pass_input,repass_input];
    for (i=0;i<items.length;i++){
         if(items[i].value===""){
             items[i].focus();
             items[i].style.borderColor="red";
             //console.log("hello"+i);
             errormess[i].innerHTML="This field is empty";
             $event.preventDefault();

         }

     }
    if(uname_input.value===""&& fname_input.value==="" &&lname_input.value===""&&email_input.value===""&&pass_input.value===""&&repass_input.value==="" ){


        errormess[0].innerHTML="User name field is empty";
        errormess[1].innerHTML="First name field is empty";
        errormess[2].innerHTML="Last name field is empty";
        errormess[3].innerHTML="Email field is  empty";
        errormess[4].innerHTML="Password field is  empty";
        errormess[5].innerHTML="Password confirmation is empty";
        uname_input.style.borderColor="red";
        fname_input.style.borderColor="red";
        lname_input.style.borderColor="red";
        email_input.style.borderColor="red";
        pass_input.style.borderColor="red";
        repass_input.style.borderColor="red";
        $event.preventDefault();
    }
    if(repass_input.value!=pass_input.value || pass_input.value.length<8 ||pass_input.value.length>20){
        errormess[4].innerHTML="Please re enter your password ";

        $event.preventDefault();
    }


}