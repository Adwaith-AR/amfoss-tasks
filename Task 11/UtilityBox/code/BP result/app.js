const HighBp = document.getElementById("HighBp")
const LowBp = document.getElementById("LowBp")
const submitBtn = document.getElementById("submitBtn")
let CTV = document.body.style.backgroundColor
let pitValue = HighBp.style.boxShadow

if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}

submitBtn.addEventListener('click', () => {
          if (HighBp.value == "" || LowBp.value == "") {
                    window.alert("Enter the reading")
           }
          else if (HighBp.value <= 120 && LowBp.value <= 80) {
                    ShowResult("green")

          }
          else if (HighBp.value <= 129 && LowBp.value <= 80) {
                    ShowResult("#ffcc32")

          }
          else if (HighBp.value <= 139 && LowBp.value <= 89) {
                    ShowResult("#ff9800")

          }
          else if (HighBp.value > 139 && LowBp.value > 89) {
                    ShowResult("red")

          }
})
function ShowResult(Color) {
          HighBp.style.backgroundColor = Color
          HighBp.style.boxShadow = "none"
          LowBp.style.boxShadow = "none"
          LowBp.style.backgroundColor = Color
          setTimeout(() => {
                    HighBp.style.backgroundColor = CTV
                    HighBp.style.boxShadow = pitValue
                    LowBp.style.boxShadow = pitValue
                    LowBp.style.backgroundColor = CTV
          }, 1000);
          HighBp.style.backgroundColor = Color
          HighBp.style.boxShadow = "none"
          LowBp.style.boxShadow = "none"
          LowBp.style.backgroundColor = Color
          setTimeout(() => {
                    HighBp.style.backgroundColor = CTV
                    HighBp.style.boxShadow = pitValue
                    LowBp.style.boxShadow = pitValue
                    LowBp.style.backgroundColor = CTV
          }, 1000);
}