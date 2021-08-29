var mejores_resultados_dataframe = JSON.parse((JSON.parse(document.getElementById('mejores_resultados_dataframe').textContent)));

var estrategias_comparadas = JSON.parse(JSON.parse(document.getElementById('estrategias_comparadas').textContent));

var lista_10_mejores_dataframes = JSON.parse(JSON.parse(document.getElementById('lista_10_mejores_dataframes').textContent));




var nombre_estrategias = []
var columnas_estrategias = []
for (let indice = 0; indice < lista_10_mejores_dataframes.length; indice++) {
    if (indice == 0) {

        nombre_estrategias.push("capital_estrategia_" + lista_10_mejores_dataframes[indice]);
        columnas_estrategias.push(lista_10_mejores_dataframes[indice]);
    }
    else {

        nombre_estrategias.push("capital_estrategia_" + lista_10_mejores_dataframes[indice]);
        columnas_estrategias.push(lista_10_mejores_dataframes[indice]);


    };
}



function funcion_datos_grafico_barras_medias_moviles() {
    var estrategias = []
    const data_medias = {}
    const Buy_and_Hold = []

    for (contador in nombre_estrategias) {
        var estrategia_individual = []
        for (let indice = 0; indice < estrategias_comparadas.length; indice++) {

            const estrategia_dia_dia = []
            if (contador == 0) {

                estrategia_dia_dia.push(estrategias_comparadas[indice].Date);
                estrategia_dia_dia.push(estrategias_comparadas[indice][nombre_estrategias[contador]]);

            }
            else {
                estrategia_dia_dia.push(estrategias_comparadas[indice].Date);
                estrategia_dia_dia.push(estrategias_comparadas[indice][nombre_estrategias[contador]]);
            }
            estrategia_individual.push(estrategia_dia_dia)
        }
        estrategias.push(estrategia_individual)

    }

    for (let indice = 0; indice < estrategias_comparadas.length; indice++) {
        var estrategia_individual_buy_hold = []
        estrategia_individual_buy_hold.push(estrategias_comparadas[indice].Date);
        estrategia_individual_buy_hold.push(estrategias_comparadas[indice].Buy_and_Hold);
        Buy_and_Hold.push(estrategia_individual_buy_hold)
    }
    series = [{
        name: "Buy_and_Hold",
        data: Buy_and_Hold
    }]
    console.log(estrategias)

    for (contador in columnas_estrategias) {
        if (contador < 10) {
            serie = {
                name: "Estrategia " + columnas_estrategias[contador],
                data: estrategias[contador]
            }
            series.push(serie)
        }
    }
    return series;

}
var estrategias = funcion_datos_grafico_barras_medias_moviles()



var titulos_tabla = []
for (var key in mejores_resultados_dataframe[0]) {
    titulos_tabla.push(key);
};
titulos_tabla.push('REVISAR')



function crea_boton(nombre) {
    var btn = document.createElement('input');
    btn.type = "button";
    btn.innerHTML = "HOLI";
    btn.innerText = "HOLI";
    btn.className = "btn";
    btn.id = "btn" + nombre;
    //btn.onclick = (function (entry) { return function () { chooseUser(entry); } })(entry);
    return btn
};

function crea_submit(nombre) {
    var form = document.createElement("form");
    form.method = "GET";
    form.action = "/testeo_masivo_corrido_revisada/";
    document.body.appendChild(form);
    var s = document.createElement("input");
    s.setAttribute("type", "submit");
    s.setAttribute("value", nombre);
    s.setAttribute('name', 'nombre');
    form.appendChild(s);

    return form
};

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
    for (let indice = 0; indice < mejores_resultados_dataframe.length; indice++) {
        if (indice < 10) {
            var tr = tbl.insertRow();
            for (let indice2 in titulos_tabla) {
                var td = tr.insertCell();
                if (titulos_tabla[indice2] == 'REVISAR') {
                    td.appendChild(crea_submit(mejores_resultados_dataframe[indice].Estrategia));
                    //console.log(mejores_resultados_dataframe[indice].Estrategia)
                }
                else {
                    td.appendChild(document.createTextNode(mejores_resultados_dataframe[indice][titulos_tabla[indice2]]));
                    td.style.border = '1px solid black';
                }
            }
        }
    }
    body.appendChild(tbl);
}
tableCreate();




Highcharts.chart('container', {

    title: {
        text: 'Mejores estrategias contra Buy and Hold'
    },



    yAxis: {
        title: {
            text: 'Number of Employees'
        }
    },

    xAxis: {
        type: 'datetime'
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 2018
        }
    },



    series: estrategias,

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});



/* var boton = document.getElementById('btn30_86')
boton.addEventListener("click", function () {
    var form = document.createElement("form");

    var element1 = document.createElement("input");
    element1.value = "HOLIS";
    form.appendChild(element1);
    body.appendChild(form);
    form.submit();
}); */