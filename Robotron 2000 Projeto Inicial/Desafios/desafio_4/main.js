var btnTintas = document.querySelector("[data-estoque]")

btnTintas.addEventListener("click", () => {
    var listaTintas = document.querySelector("[data-lista]")

    if(listaTintas.style.display === "none") {
        listaTintas.style.display = "block"
    } else {
        listaTintas.style.display = "none"
    }
})