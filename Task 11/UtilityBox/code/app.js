const themeBtn = document.getElementById("theme")

const tools = [
          "calculator",
          "Password Generator",
          "Stop Watch",
          "Random Number",
          "Markdown previewer",
          "Unit converter",
          "Currency Converter",
          "BP result",
          "QR Genarator"
]



if (localStorage.getItem("theme") == "null") {
          localStorage.setItem("theme", "light")
}
else if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
          themeBtn.innerHTML = `<img id="themeIcon" src="./img/moon.png" alt="">`
}
else {
          document.body.setAttribute("data-theme", "light")
          themeBtn.innerHTML = `<img id="themeIcon" src="./img/sun.png" alt="">`
}

function ItemCardBuilder(tools) {
          const container = document.getElementById("tools_container")
          const itemsCreated = []
          for (let i = 0; i < tools.length; i++) {
                    itemsCreated.push(`<a href="./${tools[i]}/index.html"><div class="tools" id="${tools[i]}"><img src="./${tools[i]}/img/${tools[i]}.svg"alt="logo"><h4>${tools[i]}</h4></div></a>`)

          }
          container.innerHTML = itemsCreated.join("")
}


themeBtn.addEventListener("click", function () {
          let curentTheme = document.body.getAttribute("data-theme");
          if (curentTheme == "dark") {
                    document.body.setAttribute("data-theme", "light")
                    localStorage.setItem("theme", "light")
                    themeBtn.innerHTML = `<img id="themeIcon" src="./img/sun.png" alt="">`
          }
          else {
                    localStorage.setItem("theme", "dark")
                    document.body.setAttribute("data-theme", "dark")
                    themeBtn.innerHTML = `<img id="themeIcon" src="./img/moon.png" alt="">`
          }
})

ItemCardBuilder(tools)
const fuseOptions = { keys: ['name'], threshold: 0.4 };
const fuse = new Fuse(tools, fuseOptions);
function search() {
          const value = document.getElementById("searchBox")
          const searchResults = fuse.search(value.value);


          if (value.value == "") {
                    ItemCardBuilder(tools)

          }
          else if (searchResults.length > 0) {
                    let bestMatch = []

                    for (let j = 0; j < searchResults.length; j++) {
                              bestMatch.push(searchResults[j].item);
                    }
                    ItemCardBuilder(bestMatch)
                    value.value = "";

          } else {
                    ItemCardBuilder([])
                    value.value = "";
          }
};





