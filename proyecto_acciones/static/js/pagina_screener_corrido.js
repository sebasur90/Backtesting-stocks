

var resultados_screener = JSON.parse(document.getElementById('result').textContent);
var encontro = new String(JSON.parse(document.getElementById('encontro').textContent));
//var encontrado = new String(encontro);



var titulos_tabla = ['ACCION', 'NOMBRE COMPLETO', 'SECTOR', 'ULTIMO PRECIO', 'SEÑAL', 'DIA SEÑAL']



if (encontro == new String("NO").valueOf()) {

    var div_encontro = document.getElementById('div_encontro');
    div_encontro.innerHTML = "<h2> NO SE ENCONTRARON ACCIONES QUE CUMPLAN CON LA ESTRATEGIA SELECCIONADA</h2>"
} else {

    function tableCreate() {
        var body = document.getElementById('div_tabla'),
            tbl = document.createElement('table');
        tbl.style.width = '100px';
        tbl.style.border = '1px solid black';

        var thead = document.createElement('thead');
        tbl.appendChild(thead);
        for (var i = 0; i < titulos_tabla.length; i++) {
            thead.appendChild(document.createElement("th")).
                appendChild(document.createTextNode(titulos_tabla[i]));

        }
        for (let indice in resultados_screener) {

            var tr = tbl.insertRow();
            console.log(resultados_screener[indice])
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(resultados_screener[indice].nombre));
            td.style.border = '1px solid black';
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(resultados_screener[indice].nombre_completo));
            td.style.border = '1px solid black';
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(resultados_screener[indice].sector));
            td.style.border = '1px solid black';
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(resultados_screener[indice].ultimo_precio));
            td.style.border = '1px solid black';
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(resultados_screener[indice].senal));
            td.style.border = '1px solid black';
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(resultados_screener[indice].dia_senal));
            td.style.border = '1px solid black';



        }
        body.appendChild(tbl);
    }
    tableCreate();


}



