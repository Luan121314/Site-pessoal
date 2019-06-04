// const elem = document.querySelector("#res");
// const telaWelcome = document.querySelector(".launch");
// const texto = document.querySelector("#texto");
// const header = document.querySelector("#contain");
// let tempo = new Date;
// let hora = tempo.getHours();
// let str ="";

// if(hora >= 12 && hora <= 18){
//     str = "Boa tarde";
// }else if (hora >= 19  && hora < 24){
//     str ="Boa noite";
// }else if(hora >= 0 && hora <= 5 ){
//     str = "Boa Madrugada";
// }else{
//     str = "Bom dia"
// }
// elem.innerHTML =str;

// window.onload = sobeTexto;


// function sobeTexto(){
//     console.log("Entrou na função");
//     texto.classList.add("desceTeto-Ativa");
//     setInterval(function someImg(){
//         telaWelcome.classList.add("launch-desativada");
//         header.classList.add("launch-desativada");
//         setInterval(function displayNone(){
//             telaWelcome.classList.add("retiraWelcome");
//         },3000 );
//     },3000);
// }




window.onscroll = function() {myFunction()};

const header = document.querySelector(".header");
const links = document.querySelector(".contain-links");
const sticky = header.offsetTop;



function myFunction() {
  console.log("stick " +sticky);
  console.log("window " +window.pageYOffset);

  if (window.pageYOffset > ( sticky)) {
    header.classList.add("sticky");
    // links.classList.add("espacarLinks");



  } else {
    header.classList.remove("sticky");
    // links.classList.remove("espacarLinks");
  }
}




