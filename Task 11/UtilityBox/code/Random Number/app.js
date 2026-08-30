const display = document.getElementById("display")
const numOfDigit = document.getElementById("numOfDigit")
const min = document.getElementById("min")
const max = document.getElementById("max")
const historyContainer = document.getElementById("historyMainContainer")
const generateBtn = document.getElementById("generateBtn")
const numOfDigitBtn = document.getElementById("numOfDigitBtn")

const minContainer = document.getElementById("minContainer")
const maxContainer = document.getElementById("maxContainer")
const numberTypeContainer = document.getElementById("numberTypeContainer")
const numOfDigitContainer = document.getElementById("numOfDigitContainer")

const typesOfNumber = ["Integers", "Decimals", "Even", "Odd"]
let historyData = []
let numOfDigitState = false

numOfDigitContainer.classList.add("blur")
max.value = 100
min.value = 1
numberType.textContent = "Integers"
numOfDigit.value = 2
if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}


function randomNumberGenerator() {

          if (Number(min.value) <= Number(max.value)) {
                    if (numOfDigitBtn.checked) {
                              if (Number(numOfDigit.value) >= 1 && Number(numOfDigit.value) <= 12) {

                                        if (max.value.length >= Number(numOfDigit.value) && min.value.length <= Number(numOfDigit.value)) {
                                                  if (numberType.textContent == "Integers") {
                                                            let selectedNum = []
                                                            for (let i = Number(min.value); i <= Number(max.value); i++) {
                                                                      if (i.toString().length == Number(numOfDigit.value)) {

                                                                                selectedNum.push(i)
                                                                      }
                                                            }

                                                            let randomNumber = Math.floor(Math.random() * (selectedNum.length - 1 + 1))
                                                            Display(selectedNum[randomNumber])
                                                  }
                                                  else if (numberType.textContent == "Decimals") {
                                                            let selectedNum = []
                                                            for (let i = Number(min.value); i <= Number(max.value); i = +(i + 0.01).toFixed(2)) {

                                                                      if ((Math.floor(i)).toString().length == Number(numOfDigit.value)) {
                                                                                selectedNum.push(i)
                                                                      }
                                                            }
                                                            let randomNumber = Math.floor(Math.random() * (selectedNum.length - 1 + 1))
                                                            Display(selectedNum[randomNumber])
                                                  }
                                                  else if (numberType.textContent == "Even") {
                                                            let selectedNum = []
                                                            for (let i = Number(min.value); i <= Number(max.value); i++) {
                                                                      if (i.toString().length == Number(numOfDigit.value)) {
                                                                                if (i % 2 == 0) {
                                                                                          selectedNum.push(i)
                                                                                }
                                                                      }
                                                            }

                                                            let randomNumber = Math.floor(Math.random() * (selectedNum.length - 1 + 1))
                                                            Display(selectedNum[randomNumber])
                                                  }
                                                  else if (numberType.textContent == "Odd") {
                                                            let selectedNum = []
                                                            for (let i = Number(min.value); i <= Number(max.value); i++) {
                                                                      if (i.toString().length == Number(numOfDigit.value)) {
                                                                                if (i % 2 == 0) {
                                                                                          selectedNum.push(i)
                                                                                }
                                                                      }
                                                            }

                                                            let randomNumber = Math.floor(Math.random() * (selectedNum.length - 1 + 1))
                                                            Display(selectedNum[randomNumber])
                                                  }
                                                  

                                        }
                                        else {
                                                  generateBtn.disabled = true
                                                  maxContainer.classList.add("shake")
                                                  numOfDigitContainer.classList.add("shake")
                                                  setTimeout(() => {
                                                            numOfDigitContainer.classList.remove("shake")
                                                            maxContainer.classList.remove("shake")
                                                            generateBtn.disabled = false
                                                            window.alert("keep your max value's number of digits less than or equal to the no of digit you selected and greater than  or equal to the number of digits of the min value ");
                                                            reset()
                                                  }, 500);
                                        }
                              }
                    }
                    else {
                              if (numberType.textContent == "Integers") {
                                        let randomNumber = Math.floor(Math.random() * (Number(max.value) - Number(min.value) + 1)) + Number(min.value)
                                        Display(randomNumber)
                              }
                              else if (numberType.textContent == "Decimals") {
                                        let randomNumber = (Math.random() * (Number(max.value) - Number(min.value) + 1)).toFixed(1) + Number(min.value)
                                        Display(randomNumber)
                              }
                              else if (numberType.textContent == "Even") {
                                        let selectedNum = []
                                        for (let i = Number(min.value); i <= Number(max.value); i++) {
                                                  if (i % 2 == 0) {
                                                            selectedNum.push(i)
                                                  }

                                        }
                                        let randomNumber = Math.floor(Math.random() * (selectedNum.length - 1 + 1))
                                        Display(selectedNum[randomNumber])
                              }
                              else if (numberType.textContent == "Odd") {
                                        let selectedNum = []
                                        for (let i = Number(min.value); i <= Number(max.value); i++) {
                                                  if (i % 2 != 0) {
                                                            selectedNum.push(i)
                                                  }

                                        }
                                        let randomNumber = Math.floor(Math.random() * (selectedNum.length - 1 + 1))
                                        Display(selectedNum[randomNumber])
                              }

                    }


          }
          else {
                    generateBtn.disabled = true
                    minContainer.classList.add("shake")
                    maxContainer.classList.add("shake")

                    setTimeout(() => {
                              min.value = 1
                              max.value = 10
                              minContainer.classList.remove("shake")
                              maxContainer.classList.remove("shake")
                              generateBtn.disabled = false
                              window.alert("Keep the minimum value less than the maximum value or vice versa");
                    }, 500);


          }


}

function numOfDigitStateFun() {
          if (numOfDigitBtn.checked) {
                    numOfDigitBtn.checked = true;
                    numOfDigitContainer.classList.remove("blur")
          }
          else {
                    numOfDigitBtn.checked = false;
                    numOfDigitContainer.classList.add("blur")
          }
}


function numberTypeForward() {
          let currentType = typesOfNumber.indexOf(numberType.textContent)
          if (currentType != typesOfNumber.length-1) {
                    numberType.textContent = typesOfNumber[currentType + 1]
          }

}
function numberTypeBackward() {

          let currentType = typesOfNumber.indexOf(numberType.textContent)
          if (currentType != 0) {
                    numberType.textContent = typesOfNumber[currentType - 1]
          }
}
function numberIncrease(id) {
          const displayValue = document.getElementById(id)
          if (id !== "numOfDigit") {
                    const displayValue = document.getElementById(id)
                    displayValue.value = Number(displayValue.value) + 1
          }
          if (id == "numOfDigit") {
                    const displayValue = document.getElementById(id)
                    if (Number(displayValue.value < 12)) {
                              displayValue.value = Number(displayValue.value) + 1

                    }

          }

}

function numberDecrease(id) {
          if (id !== "numOfDigit") {
                    const displayValue = document.getElementById(id)
                    displayValue.value = Number(displayValue.value) - 1
          }
          if (id == "numOfDigit") {
                    const displayValue = document.getElementById(id)
                    if (Number(displayValue.value > 1)) {
                              numOfDigitToDisplay.textContent = `${Number(displayValue.value) - 1}-Degit Number`
                              displayValue.value = Number(displayValue.value) - 1

                    }

          }
}

function reset() {
          numOfDigitBtn.checked = false
          numOfDigitStateFun()
          clearHistory()
          display.textContent = 0
          max.value = 10
          min.value = 1
          numberType.textContent = "Integers"
          numOfDigit.value = 2
}
function clearHistory() {
          historyData = []
          historyContainer.innerHTML = ""
}

function Display(randomNumber) {
          display.textContent = randomNumber
          historyData = historyData.reverse()
          historyData.push(`<div class="historyData"><p>${randomNumber}</p><button>😒</button></div>`)

          historyContainer.innerHTML = historyData.reverse().join("")
}