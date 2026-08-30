const qrText = document.getElementById("InText");
const Genarate = document.getElementById("Genarate");
const qrcode = document.getElementById("qrCodeContainer");

if (localStorage.getItem("theme") == "dark") {
       
          window.alert("sorry this page does not have dark theme support")
}

Genarate.addEventListener("click", () => {

          const text = qrText.value.trim();

          if (text === "") {

                    alert("Please enter something.");

                    return;
          }


          // Remove previous QR code
          qrcode.innerHTML = "";


          // Generate QR code
          new QRCode(qrcode, {
                    text: text,

                    width: 200,
                    height: 200,
                    colorDark: "#000000",
                    colorLight: "#ffffff",

                    correctLevel:
                              QRCode.CorrectLevel.H
          });

});