var hol = document.getElementById('dropdown_estrategias');

hol.addEventListener('change', cambia);

function cambia() {
    var cabmaiaba = document.getElementById('dropdown_estrategias')

    if (cabmaiaba.value == 'CRUCE-MEDIAS') {
        var setea = document.getElementById('seteos');
        setea.style.display = "block";
        setea.innerHTML = '<div class="descripcion_estrat"> <p>El sistema de cruce de medias hace referencia a 2 medias moviles,una corta y otra larga. Cuando la corta cruza a la larga de abajo hacia arriba ,nos daria la señal para comprar la acción correspondiente. En caso de que la media movil larga ,cruce a la corta desde arriba hacia abajo ,nos daria señal de venta y debemos salir de la posicion.</p> </div>' +
            '<div name="seteos2" id="seteos2">' +
            '<input type="range" min="0" max="100" id="range1" name="range1" placeholder="140" class="rangos">' +
            '<label for="range" id="labelrange1" name="labelrange1" >Media Movil Corta desde</label><br>' +
            '<input type="range" min="0" max="100" id="range2" name="range2" class="rangos">' +
            '<label for="range" id="labelrange2" name="labelrange2">Media Movil Corta hasta </label><br>' +
            '<input type="range" min="0" max="250" id="range3" name="range3" class="rangos">' +
            '<label for="range" id="labelrange3" name="labelrange3">Media Movil Larga desde </label><br>' +
            '<input type="range" min="0" max="250" id="range4" name="range4" class="rangos">' +
            '<label for="range" id="labelrange4" name="labelrange4">Media Movil Larga hasta</label><br>'
        var listado = ['range1', 'range2', 'range3', 'range4']
        var rangos = document.getElementsByClassName("rangos")
        function cambia_rango(nombre) {
            var labelrango = document.getElementById('label' + nombre);
            var rango = document.getElementById(nombre);
            labelrango.innerText = rango.value;
            var descripcion_seteos = document.getElementById('descripcion_seteos');
            descripcion_seteos.style.display = "block";
            descripcion_seteos.innerHTML = '<p>Se probaran todas las medias moviles cortas entre ' + range1.value + ' y ' + range2.value + ', y medias moviles largas entre ' + range3.value + ' y ' + range4.value + '</p>'


        };
        rangos[0].addEventListener("change", function () { cambia_rango(listado[0]) });
        rangos[1].addEventListener("change", function () { cambia_rango(listado[1]) });
        rangos[2].addEventListener("change", function () { cambia_rango(listado[2]) });
        rangos[3].addEventListener("change", function () { cambia_rango(listado[3]) });
    }

    if (cabmaiaba.value == 'CRUCE-PRECIOS-CONTRA-MEDIA') {
        var setea = document.getElementById('seteos');
        setea.style.display = "block";
        setea.innerHTML = '<div class="descripcion_estrat"> <p>El sistema de cruce de precios contra medias, toma 2 medias, una corta para la compra\
         y otra larga para la venta. Cuando el precio cruza a la media corta de abajo hacia arriba ,nos daria la señal para comprar la acción correspondiente.\
          En caso de que el precio cruce la media movil larga hacia abajo,nos daria señal de venta y debemos salir de la posicion..</p> </div>' +
            '<div name="seteos2" id="seteos2">' +
            '<input type="range" min="0" max="100" id="range1" name="range1" placeholder="140" class="rangos">' +
            '<label for="range" id="labelrange1" name="labelrange1" >Media Movil Corta desde</label><br>' +
            '<input type="range" min="0" max="100" id="range2" name="range2" class="rangos">' +
            '<label for="range" id="labelrange2" name="labelrange2">Media Movil Corta hasta </label><br>' +
            '<input type="range" min="0" max="250" id="range3" name="range3" class="rangos">' +
            '<label for="range" id="labelrange3" name="labelrange3">Media Movil Larga desde </label><br>' +
            '<input type="range" min="0" max="250" id="range4" name="range4" class="rangos">' +
            '<label for="range" id="labelrange4" name="labelrange4">Media Movil Larga hasta</label><br>'
        var listado = ['range1', 'range2', 'range3', 'range4']
        var rangos = document.getElementsByClassName("rangos")
        function cambia_rango(nombre) {
            var labelrango = document.getElementById('label' + nombre);
            var rango = document.getElementById(nombre);
            labelrango.innerText = rango.value;
            var descripcion_seteos = document.getElementById('descripcion_seteos');
            descripcion_seteos.style.display = "block";
            descripcion_seteos.innerHTML = '<p>Se probaran  los cruces entre el precio y todas las medias moviles cortas dentro del rango ' + range1.value + ':' + range2.value + ', \
            y el precio contra todas las medias moviles largas dentro del rango ' + range3.value + ':' + range4.value + '</p>'


        };
        rangos[0].addEventListener("change", function () { cambia_rango(listado[0]) });
        rangos[1].addEventListener("change", function () { cambia_rango(listado[1]) });
        rangos[2].addEventListener("change", function () { cambia_rango(listado[2]) });
        rangos[3].addEventListener("change", function () { cambia_rango(listado[3]) });
    }

    if (cabmaiaba.value == 'MAXIMOS-Y-MINIMOS-HISTORICOS') {
        var setea = document.getElementById('seteos');
        setea.style.display = "block";
        setea.innerHTML = '<div class="descripcion_estrat"> <p>EL sistema de busqueda de maximos y minimos historicos busca los mayores maximos y los \
        menores minimos que se pueden encontrar en la cantidad de ruedas que seleccione. Por ejemplo si elijo como "Cantidad de ruedas para buscar " 100 \
        y a su vez cantidad de minimos 10 y maximos 10,el sistema me dara como resultado los 10 precios minimos y\
         maximos de las ultimas 100 ruedas . La estrategia me dará compra cuando el precio actual se encuentre dentro de los minimos y me arrojará venta cuando el \
         mismo sea parte de los 10 precios mayores</p> </div>' +
            '<div name="seteos2" id="seteos2">' +
            '<input type="range" min="50" max="200" id="range1" name="range1" placeholder="140" class="rangos">' +
            '<label for="range" id="labelrange1" name="labelrange1" >Rango minimo de dias a buscar</label><br>' +

            '<input type="range" min="0" max="50" id="range2" name="range2" class="rangos">' +
            '<label for="range" id="labelrange2" name="labelrange2">Cantidad de precios minimos a buscar desde </label><br>' +

            '<input type="range" min="0" max="50" id="range3" name="range3" class="rangos">' +
            '<label for="range" id="labelrange3" name="labelrange3">Cantidad de precios minimos a buscar hasta  </label><br>' +

            '<input type="range" min="0" max="50" id="range4" name="range4" class="rangos">' +
            '<label for="range" id="labelrange4" name="labelrange4">Cantidad de precios maximos a buscar desde</label><br>' +

            '<input type="range" min="0" max="50" id="range5" name="range5" class="rangos">' +
            '<label for="range" id="labelrange5" name="labelrange5">Cantidad de precios maximos a buscar hasta</label><br>'


        var listado = ['range1', 'range2', 'range3', 'range4', 'range5']
        var rangos = document.getElementsByClassName("rangos")
        function cambia_rango(nombre) {
            var labelrango = document.getElementById('label' + nombre);
            var rango = document.getElementById(nombre);
            labelrango.innerText = rango.value;
            var descripcion_seteos = document.getElementById('descripcion_seteos');
            descripcion_seteos.style.display = "block";
            descripcion_seteos.innerHTML = '<p>Se buscara dentro de las ultimas ' + range1.value + ' ruedas y comprobara si el precio actual se encuentra dentro de los \
            '+ range2.value + ' hasta ' + range3.value + ' minimos para dar señal de compra.' + 'Por otro lado buscara si el precio actual se encuentra \
            dentro de los '+ range3.value + ' hasta ' + range4.value + ' maximos de las ultimas ' + range1.value + ' ruedas para dar señal de venta</p>'
            /* ruedas , la cantidad de precios minimos \
            entre '+ range2.value + ':' + range3.value + 'y la cantidad de precios maximos entre ' + range4.value + ':' + range5.value + '</p>'
 */


        };
        rangos[0].addEventListener("change", function () { cambia_rango(listado[0]) });
        rangos[1].addEventListener("change", function () { cambia_rango(listado[1]) });
        rangos[2].addEventListener("change", function () { cambia_rango(listado[2]) });
        rangos[3].addEventListener("change", function () { cambia_rango(listado[3]) });
        rangos[4].addEventListener("change", function () { cambia_rango(listado[4]) });

    }


    /* rangos[0].addEventListener("change", cambia_rango(listado[0]));
    rangos[1].addEventListener("change", cambia_rango(listado[1]));
    rangos[2].addEventListener("change", cambia_rango(listado[2]));
    rangos[3].addEventListener("change", cambia_rango(listado[3]));
    console.log(rangos[0].value) */
    /* for (var i = 0; i < listado.length; i++) {
        console.log(listado[i])

        var rango = document.ge */

    /* rango.addEventListener('change', cambia_rango);
    function cambia_rango() {
        var labelrango = document.getElementById('label' + listado[i]);
        var rango = document.getElementById(listado[i])
        labelrango.innerText = rango.value
        console.log(rango.value)

    } */
}


/* var range1 = document.getElementById('range1')
var range2 = document.getElementById('range2')
var range3 = document.getElementById('range2')
var range4 = document.getElementById('range2')
range1.addEventListener('change', cambia_range1);
function cambia_range1() {
    var labelrange1 = document.getElementById('labelrange1');
    labelrange1.innerText = range1.value
}
range2.addEventListener('change', cambia_range2);
function cambia_range2() {
    var labelrange2 = document.getElementById('labelrange2');
    labelrange2.innerText = range2.value
} */

/* }
if (cabmaiaba.value == 'COMPRA-CRUCE-MEDIA-LOW-VENTA-CRUCE-MEDIA-HIGH') {
    var setea = document.getElementById('seteos');
    setea.innerHTML = '<input type="range" min="0" max="200" id="range1" name="range1" placeholder="140">' +
        '<label for="range" id="labelrange1" name="labelrange1" >Media Movil Corta Compra 1</label><br>' +
        '<input type="range" min="0" max="500" id="range2" name="range2">' +
        '<label for="range" id="labelrange2" name="labelrange2">Media Movil Corta Compra 2</label><br>' +
        '<input type="range" min="0" max="100" id="range3" name="range3">' +
        '<label for="range" id="labelrange3" name="labelrange3">Media Movil Larga Venta 1</label><br>' +
        '<input type="range" min="0" max="100" id="range4" name="range4">' +
        '<label for="range" id="labelrange4" name="labelrange4">Media Movil Larga Venta 2</label><br>'
    var range1 = document.getElementById('range1')
    var range2 = document.getElementById('range2')
    var range3 = document.getElementById('range3')
    var range4 = document.getElementById('range4')
    range1.addEventListener('change', cambia_range1);
    function cambia_range1() {
        var labelrange1 = document.getElementById('labelrange1');
        labelrange1.innerText = range1.value
    }
    range2.addEventListener('change', cambia_range2);
    function cambia_range2() {
        var labelrange2 = document.getElementById('labelrange2');
        labelrange2.innerText = range2.value
    }
    range3.addEventListener('change', cambia_range3);
    function cambia_range3() {
        var labelrange3 = document.getElementById('labelrange3');
        labelrange3.innerText = range3.value
    }
    range4.addEventListener('change', cambia_range4);
    function cambia_range4() {
        var labelrange4 = document.getElementById('labelrange4');
        labelrange4.innerText = range4.value
    }
}

if (cabmaiaba.value == 'CICLO-FOR-MAXIMOS-Y-MINIMOS-HISTORICOS') {
    var setea = document.getElementById('seteos');
    setea.innerHTML = '<input type="range" min="0" max="200" id="range1" name="range1" placeholder="140">' +
        '<label for="range" id="labelrange1" name="labelrange1" >cantidad_ruedas_minimos</label><br>' +
        '<input type="range" min="0" max="500" id="range2" name="range2">' +
        '<label for="range" id="labelrange2" name="labelrange2">cantidad_ruedas_minimos</label><br>' +
        '<input type="range" min="0" max="100" id="range3" name="range3">' +
        '<label for="range" id="labelrange3" name="labelrange3">cant_minimos</label><br>' +
        '<input type="range" min="0" max="100" id="range4" name="range4">' +
        '<label for="range" id="labelrange4" name="labelrange4">cant_minimos</label><br>'
    var range1 = document.getElementById('range1')
    var range2 = document.getElementById('range2')
    var range3 = document.getElementById('range3')
    var range4 = document.getElementById('range4')
    range1.addEventListener('change', cambia_range1);
    function cambia_range1() {
        var labelrange1 = document.getElementById('labelrange1');
        labelrange1.innerText = range1.value
    }
    range2.addEventListener('change', cambia_range2);
    function cambia_range2() {
        var labelrange2 = document.getElementById('labelrange2');
        labelrange2.innerText = range2.value
    }
    range3.addEventListener('change', cambia_range3);
    function cambia_range3() {
        var labelrange3 = document.getElementById('labelrange3');
        labelrange3.innerText = range3.value
    }
    range4.addEventListener('change', cambia_range4);
    function cambia_range4() {
        var labelrange4 = document.getElementById('labelrange4');
        labelrange4.innerText = range4.value
    }
}

if (cabmaiaba.value == 'CRUCE-PRECIOS-CONTRA-MEDIA') {
    var setea = document.getElementById('seteos');
    setea.innerHTML = '<input type="range" min="0" max="200" id="range1" name="range1" placeholder="140">' +
        '<label for="range" id="labelrange1" name="labelrange1" >Media Movil Corta</label><br>' +
        '<input type="range" min="0" max="500" id="range2" name="range2">' +
        '<label for="range" id="labelrange2" name="labelrange1">Media Movil Larga</label><br>'
    var range1 = document.getElementById('range1')
    var range2 = document.getElementById('range2')
    range1.addEventListener('change', cambia_range1);
    function cambia_range1() {
        var labelrange1 = document.getElementById('labelrange1');
        labelrange1.innerText = range1.value
    }
    range2.addEventListener('change', cambia_range2);
    function cambia_range2() {
        var labelrange2 = document.getElementById('labelrange2');
        labelrange2.innerText = range2.value
    }

}
; */