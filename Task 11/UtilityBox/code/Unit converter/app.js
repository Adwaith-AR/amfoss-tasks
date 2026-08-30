const type = document.getElementById("typeContainer")
const inputContainer = document.getElementById("inputContainer")
const inputValue = document.getElementById("inUnit")
const outputValue = document.getElementById("outUnit")
const outputContainer = document.getElementById("OutputContainer")
const convertBtn = document.getElementById("ConvertBtn")
const distanceList = ["nm", "mm", "Cm", "m", "Km", "mi"]
const tempratureList = ["K", "C", "F"]
const storageList = ["b", "B", "MB", "GB", "TB",]
const areaList = [""]
const VolumeList = ["cup", "gal", "mL", "L", "kL"]
if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}
//Storage Area Volume Distance Temrature   //
function converter(unit1, unit2) {
          window.console.log("done")
          if (unit1 == unit2) {
                    outputValue.value = inputValue.value
          }
          else if (unit1 == "Cm" && unit2 == "m") {
                    outputValue.value = inputValue.value / 100
          }
          else if (unit1 == "Cm" && unit2 == "Km") {
                    outputValue.value = inputValue.value / 100000
          }
          else if (unit1 == "Cm" && unit2 == "mi") {
                    outputValue.value = inputValue.value / 160934.4
          }
          else if (unit1 == "Cm" && unit2 == "mm") {
                    outputValue.value = inputValue.value * 10
          }
          else if (unit1 == "Cm" && unit2 == "nm") {
                    outputValue.value = inputValue.value * 10000000
          }
          else if (unit1 == "m" && unit2 == "Km") {
                    outputValue.value = inputValue.value / 1000
          }
          else if (unit1 == "m" && unit2 == "Cm") {
                    outputValue.value = inputValue.value * 100
          }
          else if (unit1 == "m" && unit2 == "mi") {
                    outputValue.value = inputValue.value / 1609.344
          }
          else if (unit1 == "m" && unit2 == "mm") {
                    outputValue.value = inputValue.value * 1000
          }
          else if (unit1 == "m" && unit2 == "nm") {
                    outputValue.value = inputValue.value * 1000000000
          }
          else if (unit1 == "Km" && unit2 == "m") {
                    outputValue.value = inputValue.value * 1000
          }
          else if (unit1 == "Km" && unit2 == "Cm") {
                    outputValue.value = inputValue.value * 100000
          }
          else if (unit1 == "Km" && unit2 == "mi") {
                    outputValue.value = inputValue.value * 0.621371
          }
          else if (unit1 == "Km" && unit2 == "mm") {
                    outputValue.value = inputValue.value * 1000000
          }
          else if (unit1 == "Km" && unit2 == "") {
                    outputValue.value = inputValue.value * 1e12
          }
          else if (unit1 == "mi" && unit2 == "Km") {
                    outputValue.value = inputValue.value * 1.609344
          }
          else if (unit1 == "mi" && unit2 == "m") {
                    outputValue.value = inputValue.value * 1609.344
          }
          else if (unit1 == "mi" && unit2 == "Cm") {
                    outputValue.value = inputValue.value * 160934.4
          }
          else if (unit1 == "mi" && unit2 == "mm") {
                    outputValue.value = inputValue.value * 1609344
          }
          else if (unit1 == "mi" && unit2 == "nm") {
                    outputValue.value = inputValue.value * 1.609344e12
          }
          else if (unit1 == "mm" && unit2 == "Km") {
                    outputValue.value = inputValue.value / 1000000
          }
          else if (unit1 == "mm" && unit2 == "m") {
                    outputValue.value = inputValue.value / 1000
          }
          else if (unit1 == "mm" && unit2 == "mi") {
                    outputValue.value = inputValue.value * 1609344
          }
          else if (unit1 == "mm" && unit2 == "Cm") {
                    outputValue.value = inputValue.value / 10
          }
          else if (unit1 == "mm" && unit2 == "nm") {
                    outputValue.value = inputValue.value * 1000000
          }
          else if (unit1 == "nm" && unit2 == "Km") {
                    outputValue.value = inputValue.value / 1e12
          }
          else if (unit1 == "nm" && unit2 == "m") {
                    window.console.log("done")
                    outputValue.value = inputValue.value / 1e9
          }
          else if (unit1 == "nm" && unit2 == "mi") {
                    outputValue.value = inputValue.value / 1.609344e12
          }
          else if (unit1 == "nm" && unit2 == "Cm") {
                    outputValue.value = inputValue.value / 1e7
          }
          else if (unit1 == "nm" && unit2 == "mm") {
                    outputValue.value = inputValue.value / 1e6
          }
          else if (unit1 == "K" && unit2 == "C") {
                    outputValue.value = inputValue.value - 273.15
          }
          else if (unit1 == "K" && unit2 == "F") {
                    outputValue.value = (inputValue.value - 273.15) * 9 / 5 + 32
          }
          else if (unit1 == "C" && unit2 == "K") {
                    outputValue.value = inputValue.value + 273.15;
          }
          else if (unit1 == "C" && unit2 == "F") {
                    outputValue.value = (inputValue.value * 9 / 5) + 32;
          }
          else if (unit1 == "F" && unit2 == "K") {
                    outputValue.value = (inputValue.value - 32) * 5 / 9 + 273.15;
          }
          else if (unit1 == "F" && unit2 == "C") {
                    outputValue.value = (inputValue.value - 32) * 5 / 9;
          }
          else if (unit1 == "b" && unit2 == "B") {
                    outputValue.value = inputValue.value * 8;
          }
          else if (unit1 == "b" && unit2 == "MB") {
                    outputValue.value = inputValue.value / 8000000;
          }
          else if (unit1 == "b" && unit2 == "GB") {
                    outputValue.value = inputValue.value / 8000000000;
          }
          else if (unit1 == "b" && unit2 == "TB") {
                    outputValue.value = inputValue.value / 8000000000000;
          }
          else if (unit1 == "B" && unit2 == "b") {
                    outputValue.value = inputValue.value * 8;
          }
          else if (unit1 == "B" && unit2 == "MB") {
                    outputValue.value = inputValue.value / 1000000;
          }
          else if (unit1 == "B" && unit2 == "GB") {
                    outputValue.value = inputValue.value / 1000000000;
          }
          else if (unit1 == "B" && unit2 == "TB") {
                    outputValue.value = inputValue.value / 1000000000000;
          }
          else if (unit1 == "MB" && unit2 == "b") {
                    outputValue.value = inputValue.value * 8000000;
          }
          else if (unit1 == "MB" && unit2 == "B") {
                    outputValue.value = inputValue.value * 1000000;
          }
          else if (unit1 == "MB" && unit2 == "GB") {
                    outputValue.value = inputValue.value / 1000;
          }
          else if (unit1 == "MB" && unit2 == "TB") {
                    outputValue.value = inputValue.value / 1000000;
          }
          else if (unit1 == "GB" && unit2 == "b") {
                    outputValue.value = inputValue.value * 8000000000
          }
          else if (unit1 == "GB" && unit2 == "B") {
                    outputValue.value = inputValue.value * 1000000000;
          }
          else if (unit1 == "GB" && unit2 == "MB") {
                    outputValue.value = inputValue.value * 1000;
          }
          else if (unit1 == "GB" && unit2 == "TB") {
                    outputValue.value = inputValue.value / 1000;
          }
          else if (unit1 == "TB" && unit2 == "b") {
                    outputValue.value = inputValue.value * 8000000000000;
          }
          else if (unit1 == "TB" && unit2 == "B") {
                    outputValue.value = inputValue.value * 1000000000000;
          }
          else if (unit1 == "TB" && unit2 == "MB") {
                    outputValue.value = inputValue.value * 1000000;
          }
          else if (unit1 == "TB" && unit2 == "GB") {
                    outputValue.value = inputValue.value * 1000;
          }
          else if (unit1 == "cup" && unit2 == "gal") {
                    outputValue.value = inputValue.value / 16
          }
          else if (unit1 == "cup" && unit2 == "mL") {
                    outputValue.value = inputValue.value * 236.5882365
          }
          else if (unit1 == "cup" && unit2 == "L") {
                    outputValue.value = inputValue.value * 0.2365882365
          }
          else if (unit1 == "cup" && unit2 == "kL") {
                    outputValue.value = inputValue.value * 0.0002365882365
          }
          else if (unit1 == "gal" && unit2 == "cup") {
                    outputValue.value = inputValue.value * 16
          }
          else if (unit1 == "gal" && unit2 == "mL") {
                    outputValue.value = inputValue.value * 3785.411784
          }
          else if (unit1 == "gal" && unit2 == "L") {
                    outputValue.value = inputValue.value * 3.785411784
          }
          else if (unit1 == "gal" && unit2 == "kL") {
                    outputValue.value = inputValue.value * 0.003785411784
          }
          else if (unit1 == "mL" && unit2 == "cup") {
                    outputValue.value = inputValue.value / 236.5882365
          }
          else if (unit1 == "mL" && unit2 == "gal") {
                    outputValue.value = inputValue.value / 3785.411784
          }
          else if (unit1 == "mL" && unit2 == "L") {
                    outputValue.value = inputValue.value / 1000
          }
          else if (unit1 == "mL" && unit2 == "kL") {
                    outputValue.value = inputValue.value / 1000000
          }
          else if (unit1 == "L" && unit2 == "cup") {
                    outputValue.value = inputValue.value / 0.2365882365
          }
          else if (unit1 == "L" && unit2 == "gal") {
                    outputValue.value = inputValue.valueliters / 3.785411784
          }
          else if (unit1 == "L" && unit2 == "mL") {
                    outputValue.value = inputValue.value * 1000
          }
          else if (unit1 == "L" && unit2 == "kL") {
                    outputValue.value = inputValue.value / 1000
          }
          else if (unit1 == "kL" && unit2 == "cup") {
                    outputValue.value = inputValue.value / 0.0002365882365
          }
          else if (unit1 == "kL" && unit == "gal") {
                    outputValue.value = inputValue.value / 0.003785411784
          }
          else if (unit1 == "kL" && unit2 == "mL") {
                    outputValue.value = inputValue.value * 1000000
          }
          else if (unit1 == "kL" && unit2 == "L") {
                    outputValue.value = inputValue.value * 1000
          }




}

function unit(type) {
          let values = []
          if (type == "Distance") {

                    window.console.log("enter 1")
                    for (let i = 0; i < distanceList.length; i++) {
                              window.console.log("enter 2")
                              values.push(`<option value="${distanceList[i]}">${distanceList[i]}</option>`)
                              window.console.log(values)
                    }
                    window.console.log("enter 3")
                    inputContainer.innerHTML = values.join("")
                    outputContainer.innerHTML = values.join("")
                    inputContainer.value = "Cm"
                    outputContainer.value = "m"
          }
          else if (type == "Temrature") {
                    window.console.log("enter 1")
                    for (let i = 0; i < tempratureList.length; i++) {
                              window.console.log("enter 2")
                              values.push(`<option value="${tempratureList[i]}">${tempratureList[i]}</option>`)
                              window.console.log(values)
                    }
                    window.console.log("enter 3")
                    inputContainer.innerHTML = values.join("")
                    outputContainer.innerHTML = values.join("")
                    inputContainer.value = "K"
                    outputContainer.value = "C"
          }
          else if (type == "Storage") {
                    window.console.log("enter 1")
                    for (let i = 0; i < storageList.length; i++) {
                              window.console.log("enter 2")
                              values.push(`<option value="${storageList[i]}">${storageList[i]}</option>`)
                              window.console.log(values)
                    }
                    window.console.log("enter 3")
                    inputContainer.innerHTML = values.join("")
                    outputContainer.innerHTML = values.join("")
                    inputContainer.value = "MB"
          outputContainer.value = "GB"
          }
          else if (type == "Volume") {
                    window.console.log("enter 1")
                    for (let i = 0; i < VolumeList.length; i++) {
                              window.console.log("enter 2")
                              values.push(`<option value="${VolumeList[i]}">${storageList[i]}</option>`)
                              window.console.log(values)
                    }
                    window.console.log("enter 3")
                    inputContainer.innerHTML = values.join("")
                    outputContainer.innerHTML = values.join("")
                    inputContainer.value = "cup"
                    outputContainer.value = "gal"
          }
}


unit("Distance")


type.addEventListener('change', funtion = () => {
          unit(type.value)

})
convertBtn.addEventListener('click', funtion = () => {
          converter(inputContainer.value, outputContainer.value)
})