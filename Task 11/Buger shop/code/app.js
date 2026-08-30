const themeBtn = document.getElementById("themeBtn")
const logo = document.getElementById("logo")

if (localStorage.getItem("theme") == "null") {
          localStorage.setItem("theme", "dark")
          document.body.setAttribute("data-theme", "dark")
          themeBtn.innerHTML = `<img id="themeIcon" src="./img/moon.png" alt="">`
          logo.src = "./img/logo.webp"
}
else if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
          themeBtn.innerHTML = `<img id="themeIcon" src="./img/moon.png" alt="">`
          logo.src = "./img/logo.webp"
}
else {
          document.body.setAttribute("data-theme", "light")
          themeBtn.innerHTML = `<img id="themeIcon" src="./img/sun.png" alt="">`
          logo.src = "./img/logoDark.webp"
}
themeBtn.addEventListener('click', () => { 
          if (localStorage.getItem("theme") == "dark") { 
                    themeBtnState = "light"
                    localStorage.setItem("theme","light") 
                    document.body.setAttribute("data-theme", "light")
                    themeBtn.innerHTML = `<img id="themeIcon" src="./img/sun.png" alt="">`
                    logo.src = "./img/logoDark.webp"

          }
          else { 
                    themeBtnState = "dark"
                    localStorage.setItem("theme","dark") 
                    document.body.setAttribute("data-theme", "dark")
                    themeBtn.innerHTML = `<img id="themeIcon" src="./img/moon.png" alt="">`
                    logo.src = "./img/logo.webp"
          }

})