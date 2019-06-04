const btnEnviar = document.querySelector("#btnEnviar");
btnEnviar.addEventListener("click", function(){
btnEnviar.classList.remove("btn-primary");
btnEnviar.classList.add("btn-success");
btnEnviar.textContent = "Enviado com sucesso !";

  });