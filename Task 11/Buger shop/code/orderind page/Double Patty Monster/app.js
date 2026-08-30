const decrementBtn = document.getElementById("incrementBtn");
const productQuantityLabel = document.getElementById("productQuantity");
const incrementBtn = document.getElementById("decrementBtn");
const productShowPrice = document.getElementById("productPrice");
const CartBtn = document.getElementById("b1");
const OrderBtn = document.getElementById("b2");
const deleteBtn = document.getElementById("deleteBtn");
const productQuantityContainer = document.getElementById("product_quantity");
const burgerContainer = document.getElementById("bcontainer");

const C = document.getElementById("chess");
const O = document.getElementById("onions");
const T = document.getElementById("tomatoes");
const L = document.getElementById("lettuce");
const S = document.getElementById("ketchup");
const labelC = document.getElementById("labelC");
const labelO = document.getElementById("labelO");
const labelT = document.getElementById("labelT");
const labelL = document.getElementById("labelL");
const labelS = document.getElementById("labelS");
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
labelC.classList.add("item_selected")
labelO.classList.add("item_selected")
labelT.classList.add("item_selected")
labelL.classList.add("item_selected")
labelS.classList.add("item_selected")
C.checked = true
O.checked = true
T.checked = true
L.checked = true
S.checked = true
let CBtnState = true
let OBtnState = true
let TBtnState = true
let LBtnState = true
let itemList = [
          "c", "l", "o", "s", "t",
          "cl", "co", "cs", "ct", "lo", "ls", "lt", "os", "ot", "st",
          "clo", "cls", "clt", "cos", "cot", "cst", "los", "lot", "lst", "ost",
          "clos", "clot", "clst", "cost", "lost",
          "clost"]
let itemCreated = [`<img src="./img/burger.webp" id="burger" class="burgerimg">`]
for (let i = 0; i < itemList.length; i++) {
          itemCreated.push(`<img src="./img/${itemList[i]}.webp" id="${itemList[i]}" class="burgerimg">`)

}
document.getElementById("bcontainer").innerHTML = itemCreated.join("")
const burgerImg = document.querySelectorAll(".burgerimg")
const burger = document.getElementById("burger");
let SBtnState = true
let items = document.getElementById("clost");





function hideBurger() {
          burgerImg.forEach(element => {
                    element.style.display = "none "

          });
}
hideBurger();
burger.style.display = "block"
function showBurger(item_selected) {
          hideBurger()
          if (item_selected == "") {
                    burger.style.display = "block"
          }
          else {
                    document.getElementById(item_selected).style.display = "block"

          }

}
function collectData() {
          items = ""
          if (C.checked == false) {
                    items = items + "c"
          }
          if (L.checked == false) {
                    items = items + "l"
          }
          if (O.checked == false) {
                    items = items + "o"
          }
          if (S.checked == false) {
                    items = items + "s"
          }
          if (T.checked == false) {
                    items = items + "t"
          }
          window.console.log(items)
          showBurger(items)
}



C.onclick = function () {
          if (CBtnState) {
                    CBtnState = false;
                    labelC.classList.remove("item_selected")
          }
          else {
                    CBtnState = true;
                    labelC.classList.add("item_selected")

          }
          burgerContainer.classList.add("blur")

          setTimeout(() => {
                    collectData()
                    burgerContainer.classList.add("anti_blur")
                    burgerContainer.classList.remove("blur")

          }, 500);
          burgerContainer.classList.remove("anti_blur")
}
O.onclick = function () {
          if (OBtnState) {
                    OBtnState = false;
                    labelO.classList.remove("item_selected")
          }
          else {
                    OBtnState = true;
                    labelO.classList.add("item_selected")

          }
          burgerContainer.classList.add("blur")

          setTimeout(() => {
                    collectData()
                    burgerContainer.classList.add("anti_blur")
                    burgerContainer.classList.remove("blur")

          }, 500);
          burgerContainer.classList.remove("anti_blur")
}
T.onclick = function () {
          if (TBtnState) {
                    TBtnState = false;
                    labelT.classList.remove("item_selected")
          }
          else {
                    TBtnState = true;
                    labelT.classList.add("item_selected")

          }
          burgerContainer.classList.add("blur")

          setTimeout(() => {
                    collectData()
                    burgerContainer.classList.add("anti_blur")
                    burgerContainer.classList.remove("blur")

          }, 500);
          burgerContainer.classList.remove("anti_blur")
}
L.onclick = function () {
          if (LBtnState) {
                    LBtnState = false;
                    labelL.classList.remove("item_selected")
          }
          else {
                    LBtnState = true;
                    labelL.classList.add("item_selected")

          }
          burgerContainer.classList.add("blur")

          setTimeout(() => {
                    collectData()
                    burgerContainer.classList.add("anti_blur")
                    burgerContainer.classList.remove("blur")

          }, 500);
          burgerContainer.classList.remove("anti_blur")
}
S.onclick = function () {
          if (SBtnState) {
                    SBtnState = false;
                    labelS.classList.remove("item_selected")
          }
          else {
                    SBtnState = true;
                    labelS.classList.add("item_selected")

          }
          burgerContainer.classList.add("blur")

          setTimeout(() => {
                    collectData()
                    burgerContainer.classList.add("anti_blur")
                    burgerContainer.classList.remove("blur")

          }, 300);
          burgerContainer.classList.remove("anti_blur")
}

let productQuantity = 1;

let productCost = Number(productShowPrice.textContent.slice(1));
productQuantityContainer.classList.add("orientation");
deleteBtn.classList.add("invisibility");




incrementBtn.onclick = function () {
          productQuantity++;
          productQuantityLabel.textContent = productQuantity;
          productShowPrice.textContent = "₹" + (productQuantity * productCost);
}
decrementBtn.onclick = function () {
          if (productQuantity == 1) {
                    window.alert("");
          }
          else {
                    productQuantity--;
                    productQuantityLabel.textContent = productQuantity;
                    productShowPrice.textContent = "₹" + (productQuantity * productCost);
          }
}


deleteBtn.onclick = function () {
          productQuantity = 1;
          productQuantityLabel.textContent = productQuantity;
          productShowPrice.textContent = "₹" + (productQuantity * productCost);
          productQuantityContainer.classList.add("orientation");
          deleteBtn.classList.add("invisibility");
}

setInterval(() => {
          if (productQuantity != 1) {
                    productQuantityContainer.classList.remove("orientation");
                    deleteBtn.classList.remove("invisibility");


          }
          else {
                    productQuantityContainer.classList.add("orientation");
                    deleteBtn.classList.add("invisibility");

          }
}, 100);


CartBtn.onclick = function () {
          productQuantity = 1;
          productQuantityLabel.textContent = productQuantity;
          productShowPrice.textContent = "₹" + (productQuantity * productCost);
          window.alert("Your order is added to the cart")

}
OrderBtn.onclick = function () {
          productQuantity = 1;
          productQuantityLabel.textContent = productQuantity;
          productShowPrice.textContent = "₹" + (productQuantity * productCost);
          window.alert("Your order is Registered")

}