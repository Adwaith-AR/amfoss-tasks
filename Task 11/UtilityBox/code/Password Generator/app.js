const passLength = document.getElementById("passLength");
const sliderValue = document.getElementById("sliderValue");
const upperCaseBtn = document.getElementById("UpperCase");
const lowerCaseBtn = document.getElementById("LowerCase");
const numberBtn = document.getElementById("Number");
const symbolsBtn = document.getElementById("Symbols");
const output = document.getElementById("passwordOutput")
const outputContainer = document.getElementById("outputContainer")

const upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const lowerCase = "abcdefghijklmnopqrstuvwxyz";
const number = "01234567890123456789";
const symbol = "!@#$%&*?!@#$%&*?!@#$%&*?";

let upperCaseBtnState = false;
let lowerCaseBtnState = false;
let numberBtnState = false;
let symbolsBtnState = false;

if(localStorage.getItem("theme")=="dark"){
          document.body.setAttribute("data-theme","dark")
}
else{
          document.body.setAttribute("data-theme","light")
}

upperCaseBtn.onclick = function () {
          if (upperCaseBtnState) {
                    upperCaseBtnState = false;
                    upperCaseBtn.classList.remove("activeBtn")
          }
          else {
                    upperCaseBtnState = true;
                    upperCaseBtn.classList.add("activeBtn")
          }

}
lowerCaseBtn.onclick = function () {
          if (lowerCaseBtnState) {
                    lowerCaseBtnState = false;
                    lowerCaseBtn.classList.remove("activeBtn")
          }
          else {
                    lowerCaseBtnState = true;
                    lowerCaseBtn.classList.add("activeBtn")
          }

}
numberBtn.onclick = function () {
          if (numberBtnState) {
                    numberBtnState = false;
                    numberBtn.classList.remove("activeBtn")
          }
          else {
                    numberBtnState = true;
                    numberBtn.classList.add("activeBtn")
          }

}
symbolsBtn.onclick = function () {
          if (symbolsBtnState) {
                    symbolsBtnState = false;
                    symbolsBtn.classList.remove("activeBtn")
          }
          else {
                    symbolsBtnState = true;
                    symbolsBtn.classList.add("activeBtn")
          }

}


function slider() {
          let valuePercentage = (passLength.value / passLength.max) * 100;
          passLength.style.background = `linear-gradient(to right, #5156f3 ${valuePercentage - 2}%,  #182137 ${valuePercentage - 2}%) `;

}
passLength.addEventListener('input', function () {
          slider()
          sliderValue.textContent = passLength.value

})
slider()


function PasswordGenerator() {
          let allowedChar = "";
          let generatedPassword = ""
          if (symbolsBtnState) {
                    allowedChar = allowedChar + symbol
          }
          if (numberBtnState) {
                    allowedChar = allowedChar + number
          }
          if (lowerCaseBtnState) {
                    allowedChar = allowedChar + lowerCase
          }
          if (upperCaseBtnState) {
                    allowedChar = allowedChar + upperCase
          }
          if (allowedChar != "") {
                    for (let i = 0; i < passLength.value - 1; i++) {
                              generatedPassword = generatedPassword + allowedChar[Math.floor(Math.random() * allowedChar.length)]
                              window.console.log(generatedPassword)
                    }
                    output.textContent = generatedPassword
          }
          else {
                    outputContainer.classList.add("alertBox")
                    output.classList.add("alertText")
                    setTimeout(() => {
                              output.textContent = "Select any char"

                    },70);
                    setTimeout(() => {
                              outputContainer.classList.remove("alertBox")
                              output.classList.remove("alertText")
                              output.textContent = ""

                    }, 1000);

          }


}