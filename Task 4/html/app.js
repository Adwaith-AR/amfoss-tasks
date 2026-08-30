
const url =
  "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=25&page=1&sparkline=false";

fetch(url)
  .then(response => response.json())
  .then(data => {

    const container = document.getElementById("crypto");

    data.forEach(coin => {

      container.innerHTML += `
        <div class="coin">
          <img src="${coin.image}" width="40">
<div class="inform"><h2>${coin.name}</h2>

          <p>Code: ${coin.symbol.toUpperCase()}</p>

          <p>Price: $${coin.current_price}</p>

          <p>Market Cap: $${coin.market_cap}</p>

          <p>24h Change: ${coin.price_change_percentage_24h}%</p></div>
          
        </div>
      `;

    });

  })
  .catch(error => console.error(error));
