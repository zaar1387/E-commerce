const btnMenu = document.querySelector("#btnMenu");
const menu = document.querySelector("#menu");
const icon = document.querySelector(".fa-bars")


btnMenu.addEventListener("click", ()=> {
    menu.classList.toggle("mostrar")

    if(icon.classList.contains("fa-bars")){
        icon.classList.replace("fa-bars","fa-times");
    }else{
        icon.classList.replace("fa-times","fa-bars");
    };

})

const btnSubmenu = document.querySelectorAll(".btnSubmenu")
for(let i=0; i<btnSubmenu.length; i++){
    btnSubmenu[i].addEventListener("click", function(){
        if(window.innerWidth<1024){
            const subMenu = this.nextElementSibling;
            const height = subMenu.scrollHeight;

            if(subMenu.classList.contains("desplegar")){
                subMenu.classList.remove("desplegar")
                subMenu.removeAttribute("style")
            } else{
                subMenu.classList.add("desplegar")
                subMenu.style.height = height + "px";
            }
        }
    })
}

// hago un for para recorrer porque puedo tener varios submenu, entonces hago un recorrido que detecte a cual de los submenu le hice click
//tiene que ser i<btnSubmenu para que se repita las veces necesarias depende de los submenu que haya
//if del window es para que solo funcione para movil