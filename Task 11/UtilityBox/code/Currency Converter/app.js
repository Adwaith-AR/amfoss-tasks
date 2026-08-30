const from = document.getElementById("From");
const to = document.getElementById("To");
const InAmount = document.getElementById("FromAmount");
const OutAmount = document.getElementById("ToAmount");
const converterBtn = document.getElementById("converterBtn");

const API = "10aa8d8ae22dc418e087b123";
const url = `https://v6.exchangerate-api.com/v6/${API}/latest/${from.value}`;
if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}


converterBtn.addEventListener('click', async () => {
          const url = `https://v6.exchangerate-api.com/v6/${API}/latest/${from.value}`;
          const response =await fetch(url) ;
          const data = await response.json();
          const rate = data.conversion_rates[to.value];
          const outValue = Number(InAmount.value) * rate;
          OutAmount.value = outValue
})