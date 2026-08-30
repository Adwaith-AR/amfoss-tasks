const output = document.getElementById("output")
const startBtn = document.getElementById("startBtn")
const stopBtn = document.getElementById("stopBtn")
const lapBtn = document.getElementById("lapBtn")
const lapsDataContainer = document.getElementById("lapsContainerData");
let timer = null;
let startTime = 0, elapsedTime = 0;
let isRunning = false;
let currentTimeForLaps=""
let lapsTimes =[]
if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}
function start(state) {
          if (state == "Start") {
                    startBtn.innerText = "Stop"
                    startBtn.classList.add("stopBtn")
                    startTime = Date.now() - elapsedTime;
                    timer = setInterval(update, 10)
          }
          else if (state == "Stop") {
                    startBtn.innerText = "Start"
                    startBtn.classList.remove("stopBtn")
                    clearInterval(timer)
                    elapsedTime =Date.now()-startTime
          }

}
function update() {
          let currentTime = Date.now();
          elapsedTime = currentTime - startTime;

          let hour = Math.floor(elapsedTime / (1000 * 60 * 60));
          let minute = Math.floor(elapsedTime / (1000 * 60) % 60);
          let seconds = Math.floor(elapsedTime / 1000 % 60);
          let millisecond = Math.floor(elapsedTime % 1000 / 10);

          hour = String(hour).padStart(2, "0")
          minute = String(minute).padStart(2, "0")
          seconds = String(seconds).padStart(2, "0")
          millisecond = String(millisecond).padStart(2,"0")

          output.textContent = `${hour}:${minute}:${seconds}:${millisecond}`
          currentTimeForLaps = `${hour}:${minute}:${seconds}:${millisecond}`
          

}
function reset() {
          clearInterval(timer)
          startTime = 0
          elapsedTime = 0;
          startBtn.innerText = "Start"
          startBtn.classList.remove("stopBtn")
          output.textContent = `00:00:00:00`
          lapsTimes = []
          lapsDataContainer.innerHTML = ""
         

}
function laps(){
          if(startBtn.innerText == "Stop"){
                    lapsTimes.push(`<div class="lapsData"><p>lap ${lapsTimes.length+1}</p><p>${currentTimeForLaps}</p></div>`)
                    lapsDataContainer.innerHTML= lapsTimes.join("")
          }



}


