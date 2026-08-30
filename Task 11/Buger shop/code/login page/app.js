const userName = document.getElementById("userName");
const userPassword = document.getElementById("password");
const passBtn = document.getElementById("passBtn");
const imgInvisible = document.getElementById("imgInVisible");
const imgVisible = document.getElementById("imgVisible");
const submitBtn = document.getElementById("button")
const logo  = document.getElementById("logo")
const themeBtn = document.getElementById("themeBtn")

if (localStorage.getItem("theme") == "null") {
          localStorage.setItem("theme", "light")
}
else if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
          themeBtn.innerHTML = `<img id="themeIcon" src="../img/moon.png" alt="">`
          logo.src ="../img/logo.webp"
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

let passVisibility = false;

imgVisible.classList.add("invisibility")

submitBtn.onclick = function () {
          if (userName.value == "") {
                    userName.placeholder = "Enter user name";
                    userName.classList.add("red_place_holder", "orange_border");

                    setTimeout(() => {
                              userName.classList.remove("red_place_holder");
                              userName.placeholder = "Username or Email";
                    }, 2000);



          }
          else if (userPassword.value == "") {

                    userPassword.placeholder = `Enter Your Password`;
                    userPassword.classList.add("red_place_holder");
                    setTimeout(() => {
                              userPassword.classList.remove("red_place_holder");
                              userPassword.placeholder = `Password`;
                    }, 2000);




          }
          else {
                    userName.value = "";
                    userPassword.value = "";
                    window.alert("You have Logged In");
          }
}



passBtn.onclick = function () {
          if (passVisibility) {
                    passVisibility = false;
                    imgVisible.classList.add("invisibility")
                    imgInvisible.classList.remove("invisibility")
                    userPassword.type = "password"
          }
          else {
                    userPassword.type = "text"
                    passVisibility = true;
                    imgVisible.classList.remove("invisibility")
                    imgInvisible.classList.add("invisibility")

          }
}