const P = document.getElementById("P")
const R = document.getElementById("R")
const T = document.getElementById("T")
const CalculatorBtn = document.getElementById("Calculator")
if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}

CalculatorBtn.addEventListener('click',()=>{
          window.alert((Number(P.value) * Number(R.value) * Number(T.value))/100)
          P.value = ""
          R.value = ""
          T.value = ""
})