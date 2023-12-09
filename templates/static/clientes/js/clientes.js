function add_carro(){

    container = document.getElementById("form-carro")

    html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='Placa'></div <br> <div class='col-md'> <input type='number' placeholder='Ano' class='form-control' name='Ano'></div>"

    container.innerHTML += html


}