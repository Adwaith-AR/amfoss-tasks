const userName = document.getElementById("userName");
const userEmail = document.getElementById("userEmail");
const userPassword = document.getElementById("userPassword");
const passBtn = document.getElementById("passBtn");
const passVisible = document.getElementById("passVisible");
const passInVisible = document.getElementById("passInVisible");
const userConfirmedPassword = document.getElementById("userConformPassword");
const passCBtn = document.getElementById("passCBtn");
const passCVisible = document.getElementById("passCVisible");
const passCInVisible = document.getElementById("passCInVisible");
const createBtn = document.getElementById("createBtn");
const logo = document.getElementById("logo")
const themeBtn = document.getElementById("themeBtn")

let passVisibility = false;
let passCVisibility = false;

if (localStorage.getItem("theme") == "null") {
          localStorage.setItem("theme", "light")
}
else if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
          themeBtn.innerHTML = `<img id="themeIcon" src="../img/moon.png" alt="">`
          logo.src = "../img/logo.webp"
}
else {
          document.body.setAttribute("data-theme", "light")
          themeBtn.innerHTML = `<img id="themeIcon" src="../img/sun.png" alt="">`
          logo.src = "../img/logoDark.webp"
}
themeBtn.addEventListener('click', () => {

          if (localStorage.getItem("theme") == "dark") {
                    localStorage.setItem("theme", "light")
                    document.body.setAttribute("data-theme", "light")
                    themeBtn.innerHTML = `<img id="themeIcon" src="../img/sun.png" alt="">`
                    logo.src = "../img/logoDark.webp"

          }
          else {
                    localStorage.setItem("theme", "dark")
                    document.body.setAttribute("data-theme", "dark")
                    themeBtn.innerHTML = `<img id="themeIcon" src="../img/moon.png" alt="">`
                    logo.src = "../img/logo.webp"
          }

})

passVisible.classList.add("invisible")
passCVisible.classList.add("invisible")

createBtn.onclick = function () {
          if (userName.value == "") {
                    userName.classList.add("red_placeholder", "orange_border")
                    userName.placeholder = "Enter Username";
                    setTimeout(() => {
                              userName.classList.remove("red_placeholder", "orange_border")
                              userName.placeholder = "Full Name";
                    }, 4000)

          }
          if (userEmail.value == "") {
                    userEmail.classList.add("red_placeholder", "orange_border")
                    userEmail.placeholder = "Enter Email";
                    setTimeout(() => {
                              userEmail.classList.remove("red_placeholder", "orange_border")
                              userEmail.placeholder = "Email";
                    }, 4000)

          }
          if (userPassword.value == "") {
                    userPassword.classList.add("red_placeholder", "orange_border")
                    userPassword.placeholder = "Enter password";
                    setTimeout(() => {
                              userPassword.classList.remove("red_placeholder", "orange_border")
                              userPassword.placeholder = "Password";
                    }, 4000)

          } 
          if (userConfirmedPassword.value == "") {
                    userConfirmedPassword.classList.add("red_placeholder", "orange_border")
                    userConfirmedPassword.placeholder = "Enter password";
                    setTimeout(() => {
                              userConfirmedPassword.classList.remove("red_placeholder", "orange_border")
                              userConfirmedPassword.placeholder = "Password";
                    }, 4000)

          }
          if (userName.value != "" && userEmail.value != "" && userPassword.value != "" && userConfirmedPassword.value != "" ){
                    userName.value = "";
                    userEmail.value = "";
                    userPassword.value = "";
                    userConfirmedPassword.value = "";
                    window.alert("you have logged in")
          }


}
passBtn.onclick = function(){
          if (passVisibility){

                    passVisibility = false;
                    passVisible.classList.add("invisible");
                    passInVisible.classList.remove("invisible");
                    userPassword.type = "password";
          }
          else{
                    passVisibility = true;
                    passVisible.classList.remove("invisible");
                    passInVisible.classList.add("invisible"); 
                    userPassword.type = "text";
          }
}
passCBtn.onclick = function(){
          if (passCVisibility){
                    passCVisibility = false;
                    passCVisible.classList.remove("invisible");
                    passCInVisible.classList.add("invisible");
                    userConfirmedPassword.type = "password";

          }
          else{
                    passCVisibility = true;
                    passCVisible.classList.add("invisible");
                    passCInVisible.classList.remove("invisible");
                    userConfirmedPassword.type = "text"
          }
}
        
