/*  function checkScreenWidth() {
    var div = document.getElementById('menu'); // Asegúrate de seleccionar correctamente tu div
    var contenido = document.getElementById('contenido')

    const screenWidth = window.innerWidth;

    if (screenWidth > 1020) {
        div.style.display = 'grid';
        contenido.style.display = 'grid';
    }else{
        div.style.display = 'none';
    }
}

window.addEventListener('resize', checkScreenWidth);

window.addEventListener('DOMContentLoaded', checkScreenWidth);  */

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('btn-showpassword').addEventListener('click', function () {

        const input_password = document.getElementById('id_password');

        if (input_password.type === "password") {
            input_password.type = "text";
        } else {
            input_password.type = "password";
        }


    });
});


document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('button-show-menu').addEventListener('click', function () {

        var div = document.getElementById('menu')
        var contenido = document.getElementById('contenido')
        var container = document.getElementById('container')
        var desplegable = document.getElementById('desplegable')
        var button = document.getElementById('button-show-menu')

        if (div.style.display === 'none' || div.style.display === '') {


            contenido.style.display = 'none';
            container.style.gridTemplateRows = 'auto';
            desplegable.style.display = 'none'

            div.style.visibility = 'visible'
            div.classList.remove('collapsed');
            div.style.maxHeight = '100%';



        } else {

            div.classList.add('collapsed');
            div.style.maxHeight = '0';
            div.style.display = 'none';

            contenido.style.display = 'grid';
            container.style.gridTemplateRows = 'auto 1fr';
            button.innerHTML = 'Show Menu';

        }


    });
});




document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('Button-addObject-footer').addEventListener('click', function () {

        var div = document.getElementById('form-clients');
        var divtabla = document.getElementById('div-generalTable');
        var divbuscador = document.getElementById('div-searchEngine');
        var button = document.getElementById('Button-addObject-footer');

        if (divtabla.style.display === 'block') {


            div.style.display = 'block';
            divtabla.style.display = 'none'
            divbuscador.style.visibility = 'hidden'
            button.innerHTML = "Back"

        } else {

            div.style.display = 'none';
            divtabla.style.display = 'block'
            divbuscador.style.visibility = 'visible'
            button.innerHTML = "Add Clients"

        }
    });
});



document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('Button-addObject-footer').addEventListener('click', function () {
        var div = document.getElementById('form-vehicles');
        var divtabla = document.getElementById('div-generalTable');
        var divbuscador = document.getElementById('div-searchEngine');
        var button = document.getElementById('Button-addObject-footer');

        if (divtabla.style.display === 'block') {


            div.style.display = 'block';
            divtabla.style.display = 'none'
            divbuscador.style.visibility = 'hidden'
            button.innerHTML = "Back"

        } else {

            div.style.display = 'none';
            divtabla.style.display = 'block'
            divbuscador.style.visibility = 'visible'
            button.innerHTML = "Add Vehicles"

        }
    });
});


