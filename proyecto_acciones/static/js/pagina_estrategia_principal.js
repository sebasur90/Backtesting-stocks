var hol = document.getElementById('dropdown_estrategias');


hol.addEventListener('change', cambia);

function cambia() {
    var cabmaiaba = document.getElementById('dropdown_estrategias')

    if (cabmaiaba.value == 'CRUCE-MEDIAS') {
        var setea = document.getElementById('seteos');
        setea.style.display = "block";

        setea.innerHTML = '<div class="descripcion_estrat"> <p>El sistema de cruce de medias hace referencia a 2 medias moviles,una corta y otra larga. \
        Cuando la corta cruza a la larga de abajo hacia arriba ,nos daria la señal para comprar la acción correspondiente. En caso de que la media movil \
        larga ,cruce a la corta desde arriba hacia abajo ,nos daria señal de venta y debemos salir de la posicion.</p> </div>' +
            '<div name="seteos2" id="seteos2">' +
            '<input type="range" min="0" max="200" id="range1" name="range1" placeholder="140" class="rangos">' +
            '<label for="range" id="labelrange1" name="labelrange1" >Media Movil Corta</label><br>' +
            '<input type="range" min="0" max="500" id="range2" name="range2" class="rangos">' +
            '<label for="range" id="labelrange2" name="labelrange2">Media Movil Larga </label><br>'

        var listado = ['range1', 'range2']
        var rangos = document.getElementsByClassName("rangos")
        function cambia_rango(nombre) {
            var labelrango = document.getElementById('label' + nombre);
            var rango = document.getElementById(nombre);
            labelrango.innerText = rango.value;

            var descripcion_seteos = document.getElementById('descripcion_seteos');
            descripcion_seteos.style.display = "block";
            descripcion_seteos.innerHTML = '<p>Se correrá el cruce entre la media movil corta de ' + range1.value + ' y la media movil larga  ' + range2.value + '</p>'
        };
        rangos[0].addEventListener("change", function () { cambia_rango(listado[0]) });
        rangos[1].addEventListener("change", function () { cambia_rango(listado[1]) });


    }
    if (cabmaiaba.value == 'CRUCE-PRECIOS-CONTRA-MEDIA') {
        var setea = document.getElementById('seteos');
        setea.style.display = "block";

        setea.innerHTML = '<div class="descripcion_estrat"> <p>El sistema de cruce de precios contra medias, toma 2 medias, una corta para la compra y otra larga\
         para la venta. Cuando el precio cruza a la media corta de abajo hacia arriba ,nos daria la señal para comprar la acción correspondiente. En caso de que el \
         precio cruce la media movil larga hacia abajo,nos daria señal de venta y debemos salir de la posicion.</p> </div>' +
            '<div name="seteos2" id="seteos2">' +
            '<input type="range" min="0" max="200" id="range1" name="range1" placeholder="140" class="rangos">' +
            '<label for="range" id="labelrange1" name="labelrange1" >Media Movil Corta</label><br>' +
            '<input type="range" min="0" max="500" id="range2" name="range2" class="rangos">' +
            '<label for="range" id="labelrange2" name="labelrange2">Media Movil Larga </label><br>'

        var listado = ['range1', 'range2']
        var rangos = document.getElementsByClassName("rangos")
        function cambia_rango(nombre) {
            var labelrango = document.getElementById('label' + nombre);
            var rango = document.getElementById(nombre);
            labelrango.innerText = rango.value;

            var descripcion_seteos = document.getElementById('descripcion_seteos');
            descripcion_seteos.style.display = "block";
            descripcion_seteos.innerHTML = '<p>Se comprará cuando el precio cruce  la media movil corta de ' + range1.value + ' de abajo hacia arriba, y se vendera \
            cuando el precio cruce la media movil larga  ' + range2.value + ' de arriba hacia abajo</p>'
        };
        rangos[0].addEventListener("change", function () { cambia_rango(listado[0]) });
        rangos[1].addEventListener("change", function () { cambia_rango(listado[1]) });

    }

    if (cabmaiaba.value == 'MAXIMOS-Y-MINIMOS-HISTORICOS') {
        var setea = document.getElementById('seteos');
        setea.style.display = "block";

        setea.innerHTML = '<div class="descripcion_estrat"> <p>EL sistema de busqueda de maximos y minimos historicos busca los mayores maximos y los menores\
         minimos que se pueden encontrar en la cantidad de ruedas que seleccione. Por ejemplo si elijo como "Cantidad de ruedas para buscar minimos" 100 y \
         "Cantidad de ruedas para buscar maximos" 100 , y a su vez cantidad de minimos 10 y maximos 10,el sistema me dara como resultado los 10 precios minimos y maximos de las \
         ultimas 100 ruedas . La estrategia me dará compra cuando el precio actual se encuentre dentro de los minimos y me arrojará venta cuando el mismo sea parte \
         de los 10 precios mayores </p> </div>' +
            '<div name="seteos2" id="seteos2">' +
            '<input type="range" min="0" max="200" id="range1" name="range1" placeholder="140" class="rangos">' +
            '<label for="range" id="labelrange1" name="labelrange1" >Cantidad de ruedas para buscar minimos</label><br>' +
            '<input type="range" min="0" max="100" id="range2" name="range2" class="rangos">' +
            '<label for="range" id="labelrange2" name="labelrange2">Cantidad de minimos </label><br>' +
            '<input type="range" min="0" max="100" id="range3" name="range3" class="rangos">' +
            '<label for="range" id="labelrange3" name="labelrange3">Cantidad de maximos </label><br>'

        var listado = ['range1', 'range2', 'range3']
        var rangos = document.getElementsByClassName("rangos")
        function cambia_rango(nombre) {
            var labelrango = document.getElementById('label' + nombre);
            var rango = document.getElementById(nombre);
            labelrango.innerText = rango.value;

            var descripcion_seteos = document.getElementById('descripcion_seteos');
            descripcion_seteos.style.display = "block";
            descripcion_seteos.innerHTML = '<p>Se buscaran los ' + range3.value + ' menores precios de las ultimas ' + range1.value + ' ruedas para comprar .\
            Se buscaran los ' + range4.value + ' mayores precios de las ultimas ' + range1.value + ' ruedas para vender .</p>'
        };
        rangos[0].addEventListener("change", function () { cambia_rango(listado[0]) });
        rangos[1].addEventListener("change", function () { cambia_rango(listado[1]) });
        rangos[2].addEventListener("change", function () { cambia_rango(listado[2]) });


    }



};