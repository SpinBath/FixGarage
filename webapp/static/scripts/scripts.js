
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

        if (divtabla.style.display === 'block' | divtabla.style.display === '') {


            div.style.display = 'block';
            divtabla.style.display = 'none';
            divbuscador.style.visibility = 'hidden';
            button.innerHTML = "Back";

        } else {

            div.style.display = 'none';
            divtabla.style.display = 'block';
            divbuscador.style.visibility = 'visible';
            button.innerHTML = "Add Vehicles";

        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('Button-addObject-footer').addEventListener('click', function () {

        var div = document.getElementById('form-vehicles');
        var divtabla = document.getElementById('div-generalTable');
        var divbuscador = document.getElementById('div-searchEngine');
        var button = document.getElementById('Button-addObject-footer');

        if (divtabla.style.display === 'block' | divtabla.style.display === '') {


            div.style.display = 'block';
            divtabla.style.display = 'none';
            divbuscador.style.visibility = 'hidden';
            button.innerHTML = "Back";

        } else {

            div.style.display = 'none';
            divtabla.style.display = 'block';
            divbuscador.style.visibility = 'visible';
            button.innerHTML = "Add Vehicles";

        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('Button-addObject-footer').addEventListener('click', function () {
        var div = document.getElementById('form-services');
        var divtabla = document.getElementById('div-generalTable');
        var divbuscador = document.getElementById('div-searchEngine');
        var button = document.getElementById('Button-addObject-footer');

        if (divtabla.style.display === 'block' | divtabla.style.display === '') {


            div.style.display = 'block';
            divtabla.style.display = 'none';
            divbuscador.style.visibility = 'hidden';
            button.innerHTML = "Back";

        } else {

            div.style.display = 'none';
            divtabla.style.display = 'block';
            divbuscador.style.visibility = 'visible';
            button.innerHTML = "Add Billing";

        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('Button-addObject-footer').addEventListener('click', function () {

        var div = document.getElementById('form-billing');
        var divtabla = document.getElementById('div-generalTable');
        var divbuscador = document.getElementById('div-searchEngine');
        var button = document.getElementById('Button-addObject-footer');

        if (divtabla.style.display === 'block' | divtabla.style.display === '') {


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



function showdata_service(value) {

    var description_data = value
    var div_info_service = document.getElementById('info-service');
    var p_info_service = document.getElementById('p-info-service');
    var div_background = document.getElementById('div-generalTable');

    if (div_info_service.style.visibility === 'hidden' | div_info_service.style.visibility === '') {

        div_info_service.style.visibility = 'visible'
        p_info_service.innerHTML = description_data
        div_background.style.filter = 'blur(2px)'

    } else {

        div_info_service.style.visibility = 'hidden'
        p_info_service.innerHTML = description_data
        div_background.style.filter = 'blur(0px)'
    }
}

function showdata_billing(value) {

    var description_data = value
    var div_info_billing = document.getElementById('info-billing');
    var p_info_billing = document.getElementById('p-info-billing');
    var div_background = document.getElementById('div-generalTable');

    if (div_info_billing.style.visibility === 'hidden' | div_info_billing.style.visibility === '') {

        div_info_billing.style.visibility = 'visible'
        p_info_billing.innerHTML = description_data
        div_background.style.filter = 'blur(2px)'

    } else {

        div_info_billing.style.visibility = 'hidden'
        p_info_billing.innerHTML = description_data
        div_background.style.filter = 'blur(0px)'
    }
}

