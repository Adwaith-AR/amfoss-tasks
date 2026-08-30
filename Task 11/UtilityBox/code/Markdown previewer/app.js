const input = document.getElementById("textarea");
const output = document.getElementById("output");

if (localStorage.getItem("theme") == "dark") {
          document.body.setAttribute("data-theme", "dark")
}
else {
          document.body.setAttribute("data-theme", "light")
}


function render() {
          output.innerHTML = DOMPurify.sanitize(marked.parse(input.value));
          window.console.log(DOMPurify.sanitize(marked.parse(input.value)))
}

input.addEventListener('input', render);
render();