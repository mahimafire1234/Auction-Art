var username_input=document.getElementById("input1");
var password_input=document.getElementById("input2");
var message=document.getElementsByClassName("message");
var submit=document.getElementById("button1");

submit.addEventListener("click",validation);

function validation($event){

    let arr=[username_input,password_input];
    for(i=0;i<arr.length;i++){
        if(arr[i].value===""){
            arr[i].focus();
            message[i].innerHTML="This field is empty";
            arr[i].style.borderColor="red";
        }
    }

    if(username_input.value==="" &&  password_input.value===""){
        message[0].innerHTML="UserName field is empty";
        message[1].innerHTML="Password field is empty";

        message[2].innerHTML="Please fill your username and password";
        username_input.style.borderColor="red";
        password_input.style.borderColor="red";
        $event.preventDefault();
    }
    if(username_input.value==="" ||  password_input.value===""){

        $event.preventDefault();
    }

}
password_input.addEventListener("keydown",()=>{
    if(password_input.value===""){
        message[1].innerHTML="Password field is empty";
        password_input.style.borderColor="red";
    }else{
        message[1].innerHTML="";
        password_input.style.borderColor="green";
    }
})

username_input.addEventListener("keydown",()=>{
    if(username_input.value===""){
        message[0].innerHTML="Username field is empty";
        username_input.style.borderColor="red";
    }else{
        message[0].innerHTML="";
        username_input.style.borderColor="green";
    }
})

