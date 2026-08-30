const container = document.getElementById("grid_contaner")
const logo = document.getElementById("logo")
const themeBtn = document.getElementById("themeBtn")

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
const burgers = [
          ["Classic Beef Burger", "120"]
          , ["Cheese Burst Burger", "135"]
          , ["BBQ Chicken Burger", "145"]
          , ["Double Patty Monster", "160"]
          , ["Veg Supreme", "200"]
          , ["Spicy Mexican Burger", "180"]
          , ["Loaded Fries", "177"]
          , ["Cheese Fries", "155"]
          , ["Chicken Nuggets", "165"]
          , ["Peri Peri Wings", "170"]
          , ["Crispy Zinger", "199"]
          , ["Paneer Tikka Burger", "143"]]


const createdBurger = []
for (let i = 0; i < 10; i++) {
          window.console.log(createdBurger)
          createdBurger.push(`<a href="../orderind page/${burgers[i][0]}/index.html"><div class="grid_child"><img class="burgerImg " src="./img/${burgers[i][0]}.webp" alt=""><div ><h1>${burgers[i][0]}</h1><p>Delicious & freshly made</p><h3>₹${burgers[i][1]}</h3><button class="Orderbtn">Order Now</button></div></div></a>`)
}
container.innerHTML = createdBurger.join("")