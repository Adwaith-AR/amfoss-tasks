const input = document.getElementById("input");
if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}

let data = ""
function btnPressed(value) {
          switch (Number(value)) {
                    case 0:
                              input.value = input.value + "0"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 1:
                              input.value = input.value + "1"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 2:
                              input.value = input.value + "2"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 3:
                              input.value = input.value + "3"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 4:
                              input.value = input.value + "4"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 5:
                              input.value = input.value + "5"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 6:
                              input.value = input.value + "6"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 7:
                              input.value = input.value + "7"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 8:
                              input.value = input.value + "8"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    case 9:
                              input.value = input.value + "9"
                              input.scrollLeft = input.scrollWidth;
                              break;
                    default:
                              if(value=="+"){
                                        input.value = input.value + "+" 
                                        input.scrollLeft = input.scrollWidth;   
                              }
                              else if(value=="-"){
                                        input.value = input.value + "-"
                                        input.scrollLeft = input.scrollWidth;
                              }
                              else if (value == "*") {
                                        input.value = input.value + "*"
                                        input.scrollLeft = input.scrollWidth;
                              }
                              else if (value == "/") {
                                        input.value = input.value + "/"
                                        input.scrollLeft = input.scrollWidth;
                              }
                              else if (value == ".") {
                                        input.value = input.value + "."
                                        input.scrollLeft = input.scrollWidth;
                              }
                              else if (value == "C") {
                                        input.value = ""
                              }
                              else if (value == "="){
                                        try{

                                                  input.value = eval(input.value)
                                        }
                                        catch{
                                                  input.value = "Error"
                                        }
                              }
                              
          }

}